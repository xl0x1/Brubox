from django.db import models


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

    # 🖼️ صورة المنتج
    image = models.ImageField(
        upload_to='products/',
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
