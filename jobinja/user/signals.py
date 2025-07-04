from django.dispatch import receiver
from django.db.models.signals import post_save, post_migrate
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from jobinja.permissions import USER_PERSMISSION_CLASSES
from .models import DummyPermissions
from django.db.utils import OperationalError, ProgrammingError

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

    try:
        group, _ = Group.objects.get_or_create(name=group_name)
        permission_codenames = USER_PERSMISSION_CLASSES.USER_GROUP_PERMISSIONS.get(group_name, [])
        perms = Permission.objects.filter(codename__in=permission_codenames)

        for perm in perms:
            group.permissions.add(perm)

        instance.groups.add(group)
    except (OperationalError, ProgrammingError):

        pass


@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    if sender.name == 'auth':
        group_names = ['Superuser', 'Technician', 'Employer', 'Employee']
        for name in group_names:
            Group.objects.get_or_create(name=name)