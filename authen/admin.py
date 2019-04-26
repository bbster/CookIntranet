from django.contrib import admin
from django.contrib.admin import ModelAdmin
from authen.models import Member


@admin.register(Member)
class MemberAdmin(ModelAdmin):
    list_display = ('username', 'password', 'first_name', 'last_name', 'phone_number')
