from rest_framework import serializers
from .models import Member


class MemberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ("id", "username", "password", "last_name", "first_name", "phone_number",)
