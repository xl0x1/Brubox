from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def products_list(request):
    """
    عرض قائمة المنتجات بترتيب تنازلي حسب تاريخ الإضافة.
    """
    products = Product.objects.all().order_by('-created_at')
    return render(request, 'products/products.html', {
        'products': products
    })


def upload_product(request):
    """
    عرض نموذج رفع منتج جديد ومعالجة البيانات بعد الإرسال.
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products_list')  # التوجيه بعد الحفظ
    else:
        form = ProductForm()

    return render(request, 'products/upload.html', {
    'form': form
    })
