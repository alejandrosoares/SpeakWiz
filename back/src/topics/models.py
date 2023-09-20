from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=100)
    enable = models.BooleanField(default=True)
    number_questions = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    premium = models.BooleanField(default=False)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.title} {self.id} '
