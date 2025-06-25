from django.urls import path
# from .views import user_welcome, user_cookies, sign_up , login
from .views import SignUp
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    # path('', user_welcome),
    # path('cookies', user_cookies),
    # path('sign-up', sign_up),
    # path('login',login),
    path("signup", SignUp.as_view()),
    path("login", TokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)