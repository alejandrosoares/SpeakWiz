from django.db import models

from languages.models import Language
from languages.utils import get_default_language


class TopicTag(models.Model):
    title = models.CharField(max_length=50)
    number_topics = models.PositiveSmallIntegerField(default=0)

    def increase_number_topics(self):
        self.number_topics += 1
        self.save()
    
    def decrease_number_topics(self):
        self.number_topics -= 1
        self.save()

    def __str__(self):
        return f'{self.title} {self.number_topics}'
    

class Topic(models.Model):
    reference = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='translations',
        help_text="Reference used to translate to other languages"
    )
    tag = models.ForeignKey(TopicTag, on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE, default=get_default_language)
    title = models.CharField(max_length=100)
    is_enabled = models.BooleanField(
        default=False, help_text="Enable it once you have reviewed the content"
    )
    is_autogenerated = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    questions = models.JSONField(default=list)

    @property
    def language_name(self):
        return self.lang.name
    
    def __str__(self):
        return f'{self.title} {self.id}'

