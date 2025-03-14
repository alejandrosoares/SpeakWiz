from django.db import models


class LLMModel(models.Model):
    name = models.CharField(max_length=100)
    temperature = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.name} - temp: {self.temperature}'


class Prompt(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    version = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def name_with_version(self):
        return f'V{self.version}: {self.name}'

    def __str__(self):
        return self.name_with_version
    

class LLMSetup(models.Model):
    model = models.ForeignKey(LLMModel, on_delete=models.CASCADE)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('model', 'prompt')

    def __str__(self): 
        return f'{self.model.name} - {self.prompt.name_with_version}'


class LLMSetupEvaluation(models.Model):
    llm_setup = models.ForeignKey(LLMSetup, on_delete=models.CASCADE)
    rating = models.FloatField()
    response_time = models.FloatField() 
    created_at = models.DateTimeField(auto_now_add=True)