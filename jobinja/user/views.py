from django.shortcuts import render
from django.http.response import HttpResponse, FileResponse
import os
import json
from user.models import User
from django.views.decorators.csrf import csrf_exempt


def user_welcome(request):
    return render(request, 'user/main.html')

def user_cookies(request):
    file = os.path.join('C:/Users/mhmmd/Desktop/test1/practice12-4/jobinja/user/templates/user/cookies.txt')
    return FileResponse(open(file, 'rb'), as_attachment=True)

@csrf_exempt
def sign_up(request):
    if request.method == "POST":
        data = json.loads(request.body)
        User.objects.create(
            name = data.get("name"),
            password = data.get("password"),
            phone_number = data.get("phone_number"),
            national_id = data.get("national_id"),
            email = data.get("email"),
            employer = data.get("employer"),
            employee = data.get("employee"),
            interested_in = data.get("interested_in"),
        )
        return HttpResponse(f"{data.get("name")} signed up.")