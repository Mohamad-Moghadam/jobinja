from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        write_only_fields= ['password']
    
    def validate(self, attrs):
        validated_data = super().validate(attrs)
        validated_data["password"] = make_password(validated_data["password"])
        return validated_data
        



