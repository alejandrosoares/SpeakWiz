from django.db import models

from llm_settings.models import BaseSetup
from languages.models import Language


class GenerationSettings(models.Model):

    is_enabled = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Generation settings'

    def __str__(self):
        return f'Enabled: {self.is_enabled}'
   

class TopicGeneratorSetup(BaseSetup):
    
    examples_to_add = models.IntegerField(default=0)


class TopicTranslatorSetup(BaseSetup):
    
    languages_to_translate = models.ManyToManyField(Language)


