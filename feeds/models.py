from django.db import models
from authen import models as user_models


class Feed(models.Model):
    id = models.AutoField(primary_key=True)
    created_id = models.ForeignKey(
        user_models.Member,
        on_delete=models.CASCADE,
        null=True
    )
    created = models.DateTimeField(auto_now_add=True, blank=None)  # 게시판 작성날짜
    updated = models.DateTimeField(auto_now=True, blank=None)  # 수정한 날짜
    title = models.CharField(max_length=500, blank=None, null=False)  # 게시판 제목
    content = models.TextField()  # 게시판 제목
    photo = models.ImageField(null=True, blank=True)  # 이미지 필드

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_filter = ['id', 'created', 'updated', 'title', 'content', 'photo']
