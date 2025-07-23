from pathlib import Path
import os
import cloudinary

# -------------------------------------------------------------
# المستخدم المخصص
# -------------------------------------------------------------
AUTH_USER_MODEL = 'core.CustomUser'

# -------------------------------------------------------------
# المسار الأساسي للمشروع
# -------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------
# مفاتيح الأمان
# -------------------------------------------------------------
SECRET_KEY = 'django-insecure-h&b+8%28wa#@3&*0w9o3*1wim8rl&h8b)n!(4@s(2sv&d_=$)^'
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# -------------------------------------------------------------
# التطبيقات المثبتة
# -------------------------------------------------------------
INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Project Apps
    'core',
    'products',
    'orders',

    # Cloudinary for Media
    'cloudinary_storage',
    'cloudinary',
]

# -------------------------------------------------------------
# الوسطاء (Middlewares)
# -------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------------------------------------------
# إعدادات القوالب
# -------------------------------------------------------------
ROOT_URLCONF = 'BruBox.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'BruBox.wsgi.application'

# -------------------------------------------------------------
# قاعدة البيانات
# -------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------------------------------------------
# تحقق كلمات المرور
# -------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------------------------------------------
# اللغة والوقت
# -------------------------------------------------------------
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# -------------------------------------------------------------
# الملفات الثابتة (Static Files)
# -------------------------------------------------------------
STATIC_URL = '/static/'

# ✅ مجلد التجميع النهائي (يُستخدم عند التشغيل: python manage.py collectstatic)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ✅ مجلد التطوير - تضع فيه ملفات CSS/JS أثناء العمل
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# -------------------------------------------------------------
# Cloudinary (وسائط media)
# -------------------------------------------------------------
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dc5vo8ik6',
    'API_KEY': '876161638251177',
    'API_SECRET': 'E4sTs38QsjdCrjJii5w3igSQkwI',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# -------------------------------------------------------------
# ملفات الوسائط (Media URL)
# -------------------------------------------------------------
MEDIA_URL = '/media/'

# -------------------------------------------------------------
# إعدادات البريد الإلكتروني (Gmail SMTP)
# -------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'albaraasalamh@gmail.com'
EMAIL_HOST_PASSWORD = 'lluv ypnn gqmv rmns'  # تأكد أنه "كلمة مرور تطبيق" وليس كلمة الحساب نفسه
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# -------------------------------------------------------------
# إعادة التوجيه بعد تسجيل الدخول / تسجيل الخروج
# -------------------------------------------------------------
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# -------------------------------------------------------------
# الإعداد الافتراضي للحقول
# -------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------------------------------------
# تهيئة Cloudinary عند التشغيل
# -------------------------------------------------------------
cloudinary.config(
    cloud_name=CLOUDINARY_STORAGE['CLOUD_NAME'],
    api_key=CLOUDINARY_STORAGE['API_KEY'],
    api_secret=CLOUDINARY_STORAGE['API_SECRET']
)
