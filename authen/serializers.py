from rest_framework import serializers
from .models import Member


class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("username", "password", "first_name", "last_name", "phone_number")


class LoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("username", "password")
