from django.urls import path
from .views import NewSuperuser

urlpatterns = [
    path('new_superuser/', NewSuperuser.as_view()),
]
