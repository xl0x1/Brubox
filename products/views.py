from django.shortcuts import render
from .models import Product

def products_list(request):
    products = Product.objects.all().order_by('-created_at')  # ترتيب تنازلي حسب الإضافة
    return render(request, 'products/products.html', {'products': products})
