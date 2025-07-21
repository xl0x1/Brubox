# Brubox/core/urls.py
from django.urls import path
from .views import home_view, signup_view, about_view

urlpatterns = [
    path('', home_view, name='home'),
    path('accounts/signup/', signup_view, name='signup'),
    path('about/', about_view, name='about'),
]
