from rest_framework.generics import CreateAPIView
from .permissions import IsSuperuser
from .serializers import UserSerializer
from django.contrib.auth.models import User


class NewSuperuser(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsSuperuser]
    queryset = User.objects.get(group = "Superuser")
