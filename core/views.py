import random
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

from products.models import Product
from .forms import EmailAuthenticationForm, CustomUserCreationForm, UserProfileForm  # ✅ أضف النموذج

User = get_user_model()


# ✅ الصفحة الرئيسية
def home_view(request):
    featured_products = Product.objects.filter(featured=True)
    return render(request, 'home.html', {'products': featured_products})


# ✅ تسجيل مستخدم جديد مع التحقق من البريد
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            verification_code = str(random.randint(100000, 999999))

            # حفظ البيانات في الجلسة
            request.session['signup_data'] = {
                'username': form.cleaned_data['username'],
                'email': form.cleaned_data['email'],
                'password': form.cleaned_data['password1'],
                'phone_number': form.cleaned_data.get('phone_number', ''),
                'country_code': form.cleaned_data.get('country_code', '+966'),
            }
            request.session['verification_code'] = verification_code

            # إرسال رمز التحقق إلى البريد
            send_mail(
                subject='🔐 رمز التحقق من بريدك',
                message=f"رمز التحقق الخاص بك هو: {verification_code}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[form.cleaned_data['email']],
                fail_silently=False,
            )

            return redirect('verify_email')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


# ✅ التحقق من رمز البريد وإنشاء المستخدم
def verify_email_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        if code == request.session.get('verification_code'):
            data = request.session.get('signup_data')
            user = User.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password'],
                phone_number=data['phone_number'],
                country_code=data['country_code']
            )
            login(request, user)

            # حذف الجلسة بعد التسجيل
            request.session.pop('signup_data', None)
            request.session.pop('verification_code', None)

            messages.success(request, 'تم التحقق من البريد وتسجيل الدخول بنجاح.')
            return redirect('home')
        else:
            messages.error(request, 'رمز التحقق غير صحيح.')

    return render(request, 'registration/verify_email.html')


# ✅ تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = EmailAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = EmailAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


# ✅ صفحة "من نحن"
def about_view(request):
    return render(request, 'about.html')


# ✅ التحقق من توفر البريد أو الاسم أو الجوال (AJAX)
def check_availability(request):
    field = request.GET.get('field')
    value = request.GET.get('value')

    if field not in ['username', 'email', 'phone_number']:
        return JsonResponse({'available': False})

    exists = User.objects.filter(**{field: value}).exists()
    return JsonResponse({'available': not exists})


# ✅ عرض وتعديل صفحة الحساب الشخصي
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم تحديث البيانات بنجاح.')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'core/profile.html', {'form': form})
