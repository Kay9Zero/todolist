from django.contrib import admin

from core.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
