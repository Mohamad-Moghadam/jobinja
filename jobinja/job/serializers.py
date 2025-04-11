from rest_framework.serializers import ModelSerializer
from job.models import Job
from django.contrib.auth.models import User


class JobSerializer(ModelSerializer):

    class Meta:
        model = Job
        fields = '__all__'
        
        
