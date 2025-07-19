from django.db import models

class Product(models.Model):
    name = models.CharField("اسم المنتج", max_length=100)
    description = models.TextField("الوصف", blank=True)
    price = models.DecimalField("السعر", max_digits=8, decimal_places=2)
    image = models.ImageField("صورة المنتج", upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
