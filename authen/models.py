from django.contrib.auth.models import AbstractUser
from django.db import models


class Member(AbstractUser):
    user_id = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
