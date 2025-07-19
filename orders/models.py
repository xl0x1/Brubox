from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="المستخدم", on_delete=models.CASCADE)
    created_at = models.DateTimeField("تاريخ الطلب", auto_now_add=True)
    is_paid = models.BooleanField("تم الدفع", default=False)

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب #{self.id} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name="الطلب", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="المنتج", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField("الكمية", default=1)

    class Meta:
        verbose_name = "عنصر طلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"
