from rest_framework import serializers
from .models import Schedules


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = ("creator", "created", "updated", "title", "detail", "cost", "photo", "username")
        creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
