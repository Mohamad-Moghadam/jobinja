from django.urls import path
from .views import user_welcome, user_cookies


urlpatterns = [
    path('', user_welcome),
    path('cookies', user_cookies),
]