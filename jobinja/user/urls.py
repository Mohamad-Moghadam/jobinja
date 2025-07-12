from django.urls import path
from .views import NewSuperuser
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('gen-token', TokenObtainPairView.as_view()),
    path('new_superuser', NewSuperuser.as_view()),
]
