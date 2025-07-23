from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, get_user_model

from products.models import Product

User = get_user_model()


# ✅ عرض السلة
def cart_view(request):
    cart = request.session.get('cart', {})

    # تأكد أن cart عبارة عن dict (وليس قائمة تالفة)
    if isinstance(cart, list):
        cart = {}

    products = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=int(product_id))
            product.quantity = quantity
            product.subtotal = product.price * quantity
            total += product.subtotal
            products.append(product)
        except (Product.DoesNotExist, ValueError):
            continue

    return render(request, 'orders/cart.html', {
        'products': products,
        'total': total
    })


# ✅ إضافة منتج إلى السلة
@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')

    try:
        quantity = int(request.POST.get('quantity', 1))
    except (ValueError, TypeError):
        quantity = 1

    cart = request.session.get('cart', {})
    if isinstance(cart, list):
        cart = {}

    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'status': 'ok'})

    return redirect('cart_view')


# ✅ حذف منتج من السلة
@require_POST
def remove_from_cart(request):
    product_id = request.POST.get('product_id')
    cart = request.session.get('cart', {})

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart

    return redirect('cart_view')


# ✅ صفحة الدفع
def checkout_view(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "سلتك فارغة.")
        return redirect('cart_view')

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        payment_method = request.POST.get('payment_method')

        # (لاحقاً يمكن حفظ الطلب في قاعدة البيانات هنا)

        # تفريغ السلة
        request.session['cart'] = {}

        return render(request, 'orders/checkout.html', {
            'success': True,
            'name': name
        })

    return render(request, 'orders/checkout.html')


# ✅ التحقق من رمز التفعيل
def verify_email_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        expected_code = request.session.get('verification_code')
        data = request.session.get('signup_data')

        if code == expected_code and data:
            try:
                user = User.objects.create_user(
                    username=data['username'],
                    email=data['email'],
                    password=data['password']
                )
                login(request, user)

                # حذف بيانات الجلسة
                del request.session['signup_data']
                del request.session['verification_code']

                messages.success(request, '✅ تم التحقق من البريد وتسجيل الدخول بنجاح.')
                return redirect('home')

            except Exception as e:
                messages.error(request, f'حدث خطأ أثناء إنشاء الحساب: {str(e)}')
                return redirect('signup')

        else:
            messages.error(request, '❌ رمز التحقق غير صحيح.')

    return render(request, 'registration/verify_email.html')
