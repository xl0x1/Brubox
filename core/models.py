from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# ✅ مدير المستخدمين المخصص
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("يجب إدخال البريد الإلكتروني")
        if not username:
            raise ValueError("يجب إدخال اسم المستخدم")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, username, password, **extra_fields)

# ✅ نموذج مستخدم مخصص بالبريد واسم المستخدم ورقم الجوال
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    username = models.CharField(max_length=150, unique=True, verbose_name="اسم المستخدم", default="user_temp")
    country_code = models.CharField(
        max_length=5,
        default='+966',
        null=True,
        blank=True,
        verbose_name="مفتاح الدولة"
    )
    phone_number = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        verbose_name="رقم الجوال"
    )
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    is_staff = models.BooleanField(default=False, verbose_name="موظف")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التسجيل")

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

# ✅ إعدادات الموقع
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

# ✅ رسائل التواصل
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    message = models.TextField(verbose_name="الرسالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإرسال")

    class Meta:
        verbose_name = "رسالة تواصل"
        verbose_name_plural = "رسائل التواصل"

    def __str__(self):
        return f"{self.name} - {self.email}"
