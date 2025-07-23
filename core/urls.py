from django.urls import path
from .views import (
    home_view,
    signup_view,
    login_view,
    about_view,
    check_availability,
    verify_email_view,  # تأكد أنك أضفت هذا
)

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('about/', about_view, name='about'),
    path('verify-email/', verify_email_view, name='verify_email'),  # مسار التحقق من البريد
    path('check_availability/', check_availability, name='check_availability'),
]
    