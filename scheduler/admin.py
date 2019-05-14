from django.contrib import admin
from django.contrib.admin import ModelAdmin
from scheduler.models import Schedules


@admin.register(Schedules)
class SchedulesAdmin(ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'creator', 'created', 'updated', 'title', 'detail', 'cost', 'photo']
