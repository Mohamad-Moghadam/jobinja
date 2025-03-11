from django.urls import path
from .views import display_job_page,job_details

urlpatterns = [
    path("", display_job_page),
    path("job-details/", job_details)

  
]
