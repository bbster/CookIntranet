from rest_framework import serializers
from authen.models import Member
from .models import Feed


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ("id", "creator", "created", "updated", "title", "content", "priority", "photo", "username")
        #  Login -> 게시글 작성 -> CurrentUserDefault가 request.user를 반환함 ->
        creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
