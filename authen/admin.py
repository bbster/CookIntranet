from django.contrib import admin
from django.contrib.admin import ModelAdmin

from authen.models import Member


@admin.register(Member)
class MemberAdmin(ModelAdmin):
    list_display = ('id', 'username')
