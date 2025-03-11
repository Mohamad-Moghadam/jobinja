from django.shortcuts import render
from django.http.response import HttpResponse, FileResponse
import os


def user_welcome(request):
    return render(request, 'user/main.html')

def user_cookies(request):
    file = os.path.join('C:/Users/mhmmd/Desktop/test1/practice12-4/jobinja/user/templates/user/cookies.txt')
    return FileResponse(open(file, 'rb'), as_attachment=True)
