from django.urls import path
# from .views import user_welcome, user_cookies, sign_up , login
from .views import CreateUser
from rest_framework_simplejwt.views import TokenObtainPairView




urlpatterns = [
    # path('', user_welcome),
    # path('cookies', user_cookies),
    # path('sign-up', sign_up),
    # path('login',login),
    path("signup", CreateUser.as_view()),
    path("login", TokenObtainPairView.as_view()),
]