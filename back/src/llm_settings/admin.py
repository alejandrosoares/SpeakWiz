from django.contrib import admin

from .models import LLMModel, Prompt, LLMSetup


admin.site.register(LLMModel)
admin.site.register(Prompt)
admin.site.register(LLMSetup)
