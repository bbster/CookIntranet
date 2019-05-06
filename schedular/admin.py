from django.contrib import admin
from django.contrib.admin import ModelAdmin
from schedular.models import Schedules


@admin.register(Schedules)
class SchedulesAdmin(ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'created_at', 'update_at', 'title', 'detail']
