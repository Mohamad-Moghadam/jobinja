from django.urls import path
from .views import user_welcome, user_cookies, sign_up


urlpatterns = [
    path('', user_welcome),
    path('cookies', user_cookies),
    path('sign-up', sign_up),
]