from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# ✅ استيراد View التسجيل اليدوي
from core.views import signup_view

urlpatterns = [
    # ⚙️ لوحة التحكم
    path('admin/', admin.site.urls),

    # 🏠 الصفحة الرئيسية و"من نحن"
    path('', include('core.urls')),

    # 🛍️ المنتجات (عرض ورفع المنتجات)
    path('products/', include('products.urls')),

    # 🛒 السلة والطلبات
    path('cart/', include('orders.urls')),

    # 🔐 نظام المصادقة (تسجيل الدخول، تسجيل الخروج، إعادة تعيين كلمة المرور)
    path('accounts/', include('django.contrib.auth.urls')),

    # 📝 تسجيل حساب جديد
    path('accounts/signup/', signup_view, name='signup'),
]

# 🖼️ دعم ملفات الميديا (صور Cloudinary أو محلية) أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 🧩 دعم ملفات static في التطوير (إن رغبت)
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
