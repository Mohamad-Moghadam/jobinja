from django.urls import path
from .views import display_job_page,job_details, add_occupation

urlpatterns = [
    path("", display_job_page),
    path("job-details/", job_details),
    path('add-occupation', add_occupation)
]
