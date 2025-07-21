from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from products.models import Product
from django.http import JsonResponse

# عرض السلة
def cart_view(request):
    cart = request.session.get('cart', {})

    # تأكد أن cart عبارة عن dict
    if isinstance(cart, list):
        cart = {}

    products = []
    total = 0

    for product_id, quantity in cart.items():
        try:
            product = Product.objects.get(id=product_id)
            product.quantity = quantity
            product.subtotal = product.price * quantity
            total += product.subtotal
            products.append(product)
        except Product.DoesNotExist:
            continue

    return render(request, 'orders/cart.html', {
        'products': products,
        'total': total
    })

# إضافة منتج إلى السلة
@require_POST
def add_to_cart(request):
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity', 1))

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

# حذف منتج من السلة
@require_POST
def remove_from_cart(request):
    product_id = request.POST.get('product_id')
    cart = request.session.get('cart', {})

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart

    return redirect('cart_view')

# صفحة الدفع
def checkout_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        payment_method = request.POST.get('payment_method')

        # (لاحقاً يمكن تخزين الطلب في قاعدة البيانات)

        request.session['cart'] = {}

        return render(request, 'orders/checkout.html', {
            'success': True,
            'name': name
        })

    return render(request, 'orders/checkout.html')
