from django.urls import path
from .views import products_list, upload_product

urlpatterns = [
    path('', products_list, name='products_list'),
    path('upload/', upload_product, name='upload_product'),
]
