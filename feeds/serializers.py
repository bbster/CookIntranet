# feeds/serializers.py
from rest_framework import serializers
from feeds import models


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = models.Feed