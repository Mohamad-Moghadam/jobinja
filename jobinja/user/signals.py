from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from jobinja.jobinja import permissions
from .models import DummyPermissions

@receiver(post_save, sender = settings.AUTH_USER_MODEL)
def assign_user_to_group(sender, instance, created, **kwargs):
    if not created:
        return

    group_name = None

    if instance.is_superuser:
        group_name = "Superuser"

    elif not instance.is_superuser and instance.is_staff:
        group_name = "Technician"

    elif instance.type == "Employer":
        group_name = "Employer"

    elif instance.type == "Employee":
        group_name = "Employee"

    if not group_name:
        return

    group, _ = Group.objects.get_or_create(name = group_name)
    Permission_codenames = permissions.USER_GROUP_PERMISSIONS.get(group_name, [])

    permission = Permission.objects.filter(codename__in = Permission_codenames)

    for perm in permission:
        if not group.permissions.filter(id = perm.id).exists():
            group.permissions.add(perm)

    instance.groups.add(group)
    instance.save()