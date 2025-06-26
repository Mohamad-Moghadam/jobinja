from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from . import models
import os
import json
from django.views.decorators.csrf import csrf_exempt
from job.models import Job
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from job.serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny , IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import filters
from django_filters.rest_framework  import DjangoFilterBackend





class LsJobs(ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filteret_fields = {'title': ['exact', 'icontains']}
    search_fields = ['title']
class CreateListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class RetrieveDestroyUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Job.objects.all()
    serializer_class = JobSerializer




# def display_job_page(request):
#     return HttpResponse("Hello and welcome this is job page!")

# def list_jobs(request):
#     jobs = models.Job.objects.filter(status="draft")
#     context = {
#         "jobs":jobs
#     }    
#     return HttpResponse("hello this is jobs!")

# def job_details(request):
#     file_jobs = os.path.join("/home/amirykta/Desktop/practice_jobinja/jobinja/job/jobs_list.pdf")
#     return FileResponse(
#         open(file_jobs, "rb"),
#         as_attachment=True
#     )

# @csrf_exempt
# def add_occupation(request, user_id: int):
#     desired_user = get_object_or_404(User, id = user_id)

#     if request.method == "POST":
#         data = json.loads(request.body)
#         Job.objects.create(
#             title = data.get("title"),
#             owner = desired_user,
#             description = data.get("description"),
#             status = data.get("status"),
#         )
#         return HttpResponse(f"{data.get("title")} was added as a new job!")