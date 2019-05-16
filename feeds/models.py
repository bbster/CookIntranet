from django.db import models
from cook_intra import settings_base

PRIORITY_CHOICES = (
        ('긴급', '긴급'),
        ('중요', '중요'),
        ('보통', '보통'),)


class Feed(models.Model):
    creator = models.ForeignKey(settings_base.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=None)  # 게시판 작성날짜
    updated = models.DateTimeField(auto_now=True, blank=None)  # 수정한 날짜
    title = models.CharField(max_length=500, blank=None, null=False)  # 게시판 제목
    content = models.TextField()  # 게시판 제목
    priority = models.CharField(max_length=5, choices=PRIORITY_CHOICES)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)  # 이미지 필드
    username = models.CharField(max_length=100, blank=True, null=True)

    # pusher modeling
    message = models.CharField(blank=True, null=True, max_length=225)
    status = models.CharField(blank=True, null=True, max_length=225)

    def __str__(self):
        return self.title

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.allowed_filter = ['id', 'creator', 'created', 'updated',
                               'title', 'content', 'priority', 'photo', 'username', 'message', 'status']

    def save(self, *args, **kwargs):  #
        if self.creator:
            self.username = self.creator.username
        return super().save(*args, **kwargs)  # real save
