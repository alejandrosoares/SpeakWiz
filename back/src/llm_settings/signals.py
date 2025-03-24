import re

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .utils.constants import SIMPLE_CURLY_BRACKETS_REGEX
from .models import Prompt


@receiver(pre_save, sender=Prompt)
def pre_save_prompt(sender, instance, **kwargs):
    template_vars = re.findall(SIMPLE_CURLY_BRACKETS_REGEX, instance.template)    
    instance.template_variables = list(set(template_vars))
