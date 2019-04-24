from django.contrib.auth.models import AbstractUser
from django.db import models


class Member(AbstractUser):
    user_id = models.CharField(max_length=30, blank=True, null=True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
