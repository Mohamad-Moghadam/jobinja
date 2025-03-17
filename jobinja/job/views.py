from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from . import models
import os
import json
from django.views.decorators.csrf import csrf_exempt
from job.models import Job

def display_job_page(request):
    return HttpResponse("Hello and welcome this is job page!")

def list_jobs(request):
    jobs = models.Job.objects.filter(status="draft")
    context = {
        "jobs":jobs
    }    
    return HttpResponse("hello this is jobs!")

def job_details(request):
    file_jobs = os.path.join("/home/amirykta/Desktop/practice_jobinja/jobinja/job/jobs_list.pdf")
    return FileResponse(
        open(file_jobs, "rb"),
        as_attachment=True
    )

@csrf_exempt
def add_occupation(request):
    if request == "POST":
        data = json.loads(request.body)
        Job.objects.create(
            title = data.get("title"),
            user_id = data.get("owner_id"),
            description = data.get("description"),
            status = data.get("status"),
        )