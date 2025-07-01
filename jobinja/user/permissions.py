from rest_framework.permissions import BasePermission

class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        return request.user.group.filter(name = "Superuser").exists()


class IsTechnician(BasePermission):
    def has_permission(self, request, view):
        return request.user.group.filter(name = "Technician").exists()