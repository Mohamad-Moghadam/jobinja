from django.shortcuts import render
from django.http.response import HttpResponse, FileResponse
import os
import json
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
<<<<<<< HEAD
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
=======
from django.contrib.auth.hashers import make_password
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveAPIView
>>>>>>> refs/remotes/origin/master
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from user.serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


class CreateUser(CreateAPIView):
    permission_classes= [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DeleteUser(DestroyAPIView):
    
    








# def user_welcome(request):
#     return render(request, 'user/main.html')

# def user_cookies(request):
#     file = os.path.join('C:/Users/mhmmd/Desktop/test1/practice12-4/jobinja/user/templates/user/cookies.txt')
#     return FileResponse(open(file, 'rb'), as_attachment=True)

# @csrf_exempt
# def sign_up(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         User.objects.create(
#             name = data.get("name"),
#             password = data.get("password"),
#             phone_number = data.get("phone_number"),
#             national_id = data.get("national_id"),
#             email = data.get("email"),
#             employer = data.get("employer"),
#             employee = data.get("employee"),
#             interested_in = data.get("interested_in"),
#         )
#         return HttpResponse(f"{data.get("name")} signed up.")
    

# @csrf_exempt
# def login(request):
#     if request.method == "POST":
#         data = json.loads(request.body)

#         name = data.get("name")
#         password = data.get("password")

#         user = User.objects.filter(name = name).first()

#         if user is None:
#             return HttpResponse("the user was not found.")
        
#         if not check_password(password,user.password):
#             return HttpResponse("your password is incorrect.")
        
#         return HttpResponse(f"welcome {name}")

#     return HttpResponse ("please enter your name and password")

# @csrf_exempt
# def login(request):
#     if request.method == "POST":
#         data = json.loads(request.body)

#         name = data.get("name"),
#         password = data.get("password")

#         user = User.objects.filter(name = name).first()

#         if user is None:
#             return HttpResponse("the user was not found.")
        
#         if not check_password(password,user.password):
#             return HttpResponse("your password is incorrect.")
        
#         return HttpResponse(f"welcome {name}")

#     return HttpResponse ("please enter your name and password")
