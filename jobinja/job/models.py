from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    STATUS_CHICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    description = models.TextField(null= True, blank= True)
    created_date = models.DateTimeField(auto_now_add= True)
    status = models.CharField(max_length=10, choices=STATUS_CHICES, default='draft')


    def __str__(self):
        return "{} - {}".format(self.title, self.created_date)
