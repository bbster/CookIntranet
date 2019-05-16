from django.contrib import admin
from django.contrib.admin import ModelAdmin
from feeds.models import Feed


@admin.register(Feed)
class SchedulesAdmin(ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'creator', 'created', 'updated', 'title', 'content', 'priority', 'photo']
