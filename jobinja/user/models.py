from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from job.models import Job

class DummyPermissions(models.Model):

    class Meta:
        permissions = [("add_superuser", "add superuser"),
                            ("list_superuser", "list superuser"),
                            ("add_technician", "add technician"),
                            ("edit_technician", "edit technician"),
                            ("delete_technician", "delete technician"),
                            ("list_technician", "list technician"),]


class Employer(models.Model):
    username = models.CharField(max_length = 100)
    national_id = models.IntegerField(max_length = 11)
    phone_number = PhoneNumberField(region = "IR")
    email = models.EmailField(blank = True, null = True)
    password = models.CharField(max_length = 100)
    companies = models.ForeignKey(Job, on_delete = models.PROTECT, related_name = "employer_companies")

    def __str__(self):
        return self.username


class Emplyee(models.Model):
    username = models.CharField(max_length = 100)
    national_id = models.IntegerField(max_length = 11)
    phone_number = PhoneNumberField(region = "IR")
    email = models.EmailField(blank = True, null = True)
    password = models.CharField(max_length = 100)
    resume = models.FileField(upload_to = "resume/")

    def __str__(self):
        return self.username