from django.urls import path
from .views import user_welcome


urlpatterns = [
    path('', user_welcome)
]