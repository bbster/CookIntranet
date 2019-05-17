from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class Member(AbstractUser):
    phone_number = models.CharField(max_length=30, blank=True, null=True)
