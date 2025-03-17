from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinLengthValidator

class User(models.Model):
    name = models.CharField(max_length = 100)
    password = models.CharField(max_length = 20, validators= [MinLengthValidator(4)], unique= True)
    phone_number = PhoneNumberField(unique=True)
    national_id = models.CharField(max_length= 11, unique = True)
    email = models.EmailField(null = True, blank = True)
    employer = models.BooleanField(default= False)
    employee = models.BooleanField(default= True)
    interested_in = models.TextField()


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete= models.CASCADE)
    avatar = models.ImageField(upload_to= 'profile_pics/')