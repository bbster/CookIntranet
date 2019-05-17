from django.db import models
from cook_intra import settings_base


class Conversation(models.Model):
    user = models.ForeignKey(settings_base.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, null=True)
    message = models.CharField(blank=True, null=True, max_length=225)
    status = models.CharField(blank=True, null=True, max_length=225)
    created_at = models.DateTimeField(auto_now=True)