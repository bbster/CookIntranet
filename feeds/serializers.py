from rest_framework import serializers
from .models import Feed


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ("id", "created", "updated", "title", "content", "photo")

        # created = models.DateTimeField(auto_now_add=True, blank=None)  # 게시판 작성날짜
        # updated = models.DateTimeField(auto_now=True, blank=None)  # 수정한 날짜
        # title = models.CharField(max_length=500, blank=None, null=False)  # 게시판 제목
        # content = models.TextField()  # 게시판 제목
        # photo = models.ImageField(null=True, blank=True)  # 이미지 필드

