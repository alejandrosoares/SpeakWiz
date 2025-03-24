from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


def _get_available_llm_models():
    from .implementations.models import AVAILABLE_LLM_MODELS
    return ((m, m) for m in AVAILABLE_LLM_MODELS)


class LLMModel(models.Model):
    name = models.CharField(max_length=100, choices=_get_available_llm_models())
    temperature = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name} - temp: {self.temperature}'


class Prompt(models.Model):
    name = models.CharField(max_length=100)
    template = models.TextField()
    version = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    template_variables = models.JSONField(default=list, blank=True)

    @property
    def name_with_version(self):
        return f'V{self.version}: {self.name}'

    def __str__(self):
        return self.name_with_version
    

class BaseSetup(models.Model):
    model = models.ForeignKey(LLMModel, on_delete=models.CASCADE)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_enabled = models.BooleanField(default=False)

    @property
    def template(self):
        return self.prompt.template
    
    class Meta:
        abstract = True

    def __str__(self): 
        return f'{self.model} - {self.prompt} - enabled: {self.enabled}'


class SetupEvaluation(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    llm_setup = GenericForeignKey('content_type', 'object_id')
    rating = models.FloatField()
    response_time = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)