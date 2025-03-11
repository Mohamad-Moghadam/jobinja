from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100, unique=True)
    national_id = models.CharField(max_length= 11, unique = True)
    email = models.EmailField(null = True, blank = True)

class profile(models.Model):
    user = models.OneToOneField(to=User, on_delete= models.CASCADE)
    avatar = models.ImageField(upload_to= 'profile_pics/')
