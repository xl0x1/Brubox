from django.db import models
from cloudinary.models import CloudinaryField


class Product(models.Model):
    # 🏷️ اسم المنتج
    name = models.CharField(
        max_length=100,
        verbose_name="اسم المنتج"
    )

    # 📝 وصف تفصيلي اختياري
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="الوصف"
    )

    # 💰 السعر (بمنزلتين عشريتين)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="السعر"
    )

    # 🖼️ صورة المنتج (باستخدام CloudinaryField)
    image = CloudinaryField(
        blank=True,
        null=True,
        verbose_name="صورة المنتج"
    )

    # ⭐ مميز في الصفحة الرئيسية
    featured = models.BooleanField(
        default=False,
        verbose_name="منتج مميز"
    )

    # 🕒 وقت الإضافة تلقائيًا
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاريخ الإضافة"
    )

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"
        ordering = ['-created_at']  # أحدث المنتجات أولًا

    def __str__(self):
        return self.name

    # ✅ دالة تعرض السعر مع رمز الريال
    def formatted_price(self):
        return f'<span class="icon-saudi_riyal"></span> {self.price}'
    formatted_price.allow_tags = True  # للسماح باستخدام HTML في الإدارة
    formatted_price.short_description = "السعر بالعملة"
