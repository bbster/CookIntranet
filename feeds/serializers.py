from rest_framework import serializers
from .models import Feed


class FeedSerializer(serializers.ModelSerializer):
    # cid = serializers.CharField(choices=models.Membe, read_only=True)
    class Meta:
        model = Feed
        fields = ("id", "creator", "created", "updated", "title", "content", "photo")
        #  Login -> 게시글 작성 -> CurrentUserDefault가 request.user를 반환함 ->
        creator = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
