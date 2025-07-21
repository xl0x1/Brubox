# Brubox/core/views.py
from django.shortcuts import render
from products.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def home_view(request):
    featured_products = Product.objects.filter(featured=True)
    return render(request, 'home.html', {'products': featured_products})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # إلى صفحة تسجيل الدخول بعد النجاح
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def about_view(request):
    return render(request, 'about.html')

