from typing import List

from django.db import models

from languages.models import Language
from topics.models import Topic


class Card(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE ,related_name='cards')
    question = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @staticmethod
    def create_cards(topic: Topic, questions: List[str]) -> None:
        Card.objects.bulk_create([
            Card(topic=topic, question=q) for q in questions
        ])

    def __str__(self):
        return f'{self.topic.title}: {self.question}'
