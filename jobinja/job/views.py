from django.shortcuts import render
from django.http import HttpResponse


def display_job_page(request):
    return HttpResponse("Hello and welcome this is job page!")


def list_jobs(request):
    pass


def job_details(request):
    pass