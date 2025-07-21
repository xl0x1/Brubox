from django.urls import path
from .views import cart_view, add_to_cart, remove_from_cart, checkout_view

urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('add/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout_view, name='checkout_view'),
]
