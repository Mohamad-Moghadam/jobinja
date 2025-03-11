from django.urls import path
from .views import display_job_page

urlpatterns = [
    path("", display_job_page),
    
  
]
