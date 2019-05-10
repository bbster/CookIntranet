from rest_framework import serializers
from .models import Feed


class FeedSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Feed
        fields = ("creator", "created", "updated", "title", "content", "priority", "photo", "username")
        #  Login -> 게시글 작성 -> CurrentUserDefault가 request.user를 반환함 ->
