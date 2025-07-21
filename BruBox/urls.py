from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🏠 الصفحة الرئيسية
    path('', include('core.urls')),

    # 🛒 المنتجات
    path('products/', include('products.urls')),

    # 📦 الطلبات والسلة
    path('cart/', include('orders.urls')),

    # 🔐 تسجيل الدخول/الخروج/كلمة المرور
    path('accounts/', include('django.contrib.auth.urls')),
]

# 🖼️ لعرض ملفات الصور أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
