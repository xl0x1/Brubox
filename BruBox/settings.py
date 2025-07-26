from pathlib import Path
import os
import cloudinary
import dj_database_url
from django.core.exceptions import ImproperlyConfigured

# -------------------------------------------------------------
# تحميل متغيرات البيئة من .env في التطوير فقط
# -------------------------------------------------------------
if os.getenv("DJANGO_PRODUCTION", "False") != "True":
    from dotenv import load_dotenv
    load_dotenv()

# -------------------------------------------------------------
# المسار الأساسي
# -------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------------------
# وضع التشغيل
# -------------------------------------------------------------
IS_PRODUCTION = os.getenv("DJANGO_PRODUCTION", "False") == "True"
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# -------------------------------------------------------------
# مفاتيح الأمان
# -------------------------------------------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
if not SECRET_KEY:
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")

ALLOWED_HOSTS = os.getenv(
    "DJANGO_ALLOWED_HOSTS_PROD" if IS_PRODUCTION else "DJANGO_ALLOWED_HOSTS",
    "brubox.onrender.com" if IS_PRODUCTION else "127.0.0.1,localhost"
).split(",")

# -------------------------------------------------------------
# المستخدم المخصص
# -------------------------------------------------------------
AUTH_USER_MODEL = 'core.CustomUser'

# -------------------------------------------------------------
# التطبيقات المثبتة
# -------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات المشروع
    'core',
    'products',
    'orders',

    # إدارة الصور
    'cloudinary_storage',
    'cloudinary',
]

# -------------------------------------------------------------
# الوسطاء
# -------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
if IS_PRODUCTION:
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        raise ImproperlyConfigured("DATABASE_URL is not set in production mode.")
    DATABASES = {
        'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv("DB_NAME"),
            'USER': os.getenv("DB_USER"),
            'PASSWORD': os.getenv("DB_PASSWORD"),
            'HOST': os.getenv("DB_HOST"),
            'PORT': os.getenv("DB_PORT", '5432'),
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
# الملفات الثابتة
# -------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -------------------------------------------------------------
# Cloudinary (الوسائط)
# -------------------------------------------------------------
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUD_API_KEY'),
    'API_SECRET': os.getenv('CLOUD_API_SECRET'),
}
if not all(CLOUDINARY_STORAGE.values()):
    raise ImproperlyConfigured("Missing one or more Cloudinary settings.")

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME'),
    api_key=os.getenv('CLOUD_API_KEY'),
    api_secret=os.getenv('CLOUD_API_SECRET')
)

MEDIA_URL = '/media/'

# -------------------------------------------------------------
# إعدادات البريد الإلكتروني
# -------------------------------------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER or 'noreply@example.com'

# -------------------------------------------------------------
# إعادة التوجيه بعد الدخول والخروج
# -------------------------------------------------------------
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'

# -------------------------------------------------------------
# الحقول الافتراضية للنماذج
# -------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------------------------------------------
# تسجيل الأخطاء في ملف
# -------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'errors.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# -------------------------------------------------------------
# طباعة وضع التشغيل (للتصحيح فقط)
# -------------------------------------------------------------
print("IS_PRODUCTION:", IS_PRODUCTION)
print("DEBUG:", DEBUG)
print("ALLOWED_HOSTS:", ALLOWED_HOSTS)
