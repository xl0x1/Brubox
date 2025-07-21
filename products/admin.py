from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # الأعمدة التي ستظهر في صفحة قائمة المنتجات
    list_display = ('name', 'price', 'featured', 'created_at')

    # إمكانية البحث بالاسم
    search_fields = ('name',)

    # فلاتر جانبية للتصفية
    list_filter = ('featured', 'created_at')

    # ترتيب افتراضي
    ordering = ('-created_at',)

    # عرض الحقول كمربعات اختيار عند تعديل المنتج
    list_editable = ('featured',)
