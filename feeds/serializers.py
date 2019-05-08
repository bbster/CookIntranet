from rest_framework import serializers
from .models import Feed


class FeedSerializer(serializers.ModelSerializer):
    # cid = serializers.CharField(choices=models.Membe, read_only=True)

    class Meta:
        model = Feed
        fields = ("id", "created_id", "created", "updated", "title", "content", "photo")
