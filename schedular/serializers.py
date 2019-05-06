from rest_framework import serializers
from .models import Schedules


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        paginate_by = 10
        ordering = ['id']
        fields = "__all__"
