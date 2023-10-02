from typing import List

from django.db import models

from topics.models import Topic


class Card(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE ,related_name='cards')
    question = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @classmethod
    def create_cards_of_topic(cls, topic: Topic, questions: List[str]) -> None:
        for question in questions:
            Card.objects.create(topic=topic, question=question)

    def __str__(self):
        return f'{self.topic.title}: {self.question}'
