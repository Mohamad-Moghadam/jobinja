from rest_framework.generics import CreateAPIView
from .permissions import IsSuperuser
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class NewSuperuser(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsSuperuser]

    def get_queryset(self):
        return User.objects.filter(groups__name = "Superuser")

    def perform_create(self, serializer):
        user = serializer.save(is_superuser=True, is_staff=True, is_active=True)
        group, _ = Group.objects.get_or_create(name="Superuser")
        user.groups.add(group)
