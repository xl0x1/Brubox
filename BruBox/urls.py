from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),           # التطبيق الرئيسي - الصفحة الرئيسية
    path('products/', include('products.urls')), # المنتجات
    path('orders/', include('orders.urls')),     # الطلبات
]
