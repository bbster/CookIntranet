from rest_framework import serializers
from .models import Schedules


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = "__all__"
