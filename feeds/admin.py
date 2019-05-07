from django.contrib import admin
from django.contrib.admin import ModelAdmin
from feeds.models import Feed


@admin.register(Feed)
class SchedulesAdmin(ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'created', 'updated', 'title', 'content', 'photo']
