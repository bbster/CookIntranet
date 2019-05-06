from django.db import models


class Schedules(models.Model):
    created_at = models.DateField(auto_now_add=True)  # 생성 날짜 및 시간
    update_at = models.DateTimeField(auto_now=True)  # 수정한 날짜 및 시간
    title = models.CharField(max_length=500, blank=None)  # 제목
    detail = models.TextField()  # 일정 상세
    money = models.CharField(max_length=30, blank=None)  # 대금
    photo = models.ImageField(null=True, blank=True)  # 이미지 업로드 # 한장만 가능..
    saw = models.IntegerField(null=True, blank=True)  # 조회수

    def __str__(self):
        return self.title
