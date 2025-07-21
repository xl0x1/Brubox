from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100, verbose_name="اسم الموقع")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True, verbose_name="الشعار")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    phone = models.CharField(max_length=20, verbose_name="رقم الجوال")
    address = models.TextField(verbose_name="العنوان")

    class Meta:
        verbose_name = "إعدادات الموقع"
        verbose_name_plural = "الإعدادات العامة"

    def __str__(self):
        return self.site_name

# ✅ أضف هذا الموديل أيضًا لحل الخطأ
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    message = models.TextField(verbose_name="الرسالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")

    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"

    def __str__(self):
        return f"{self.name} - {selfemail}"
