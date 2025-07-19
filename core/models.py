from django.db import models

class ContactMessage(models.Model):
    name = models.CharField("الاسم", max_length=100)
    email = models.EmailField("البريد الإلكتروني")
    message = models.TextField("الرسالة")
    created_at = models.DateTimeField("تاريخ الإرسال", auto_now_add=True)

    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"

    def __str__(self):
        return self.name
