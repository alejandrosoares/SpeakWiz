from django.db import models

from users.models import User


def default_user_preference_field():
    return {}

# {topic: {'1':}}


class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    preferences = models.JSONField(default=default_user_preference_field)
