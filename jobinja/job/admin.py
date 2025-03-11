from django.contrib import admin
from job.models import Job


class JobAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "status")
    list_filter = ("title", "owner")
    search_fields = ("title",)


admin.site.register(Job, JobAdmin)




