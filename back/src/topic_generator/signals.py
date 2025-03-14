from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TopicGeneratorSetup, TopicTranslatorSetup


@receiver(post_save, sender=TopicGeneratorSetup)
def post_save_topicgeneratorsetup(sender, instance, created, **kwargs):
    if instance.enabled:
        _disable_remaining_instances(instance)


@receiver(post_save, sender=TopicTranslatorSetup)
def post_save_topictranslationsetup(sender, instance, created, **kwargs):
    if instance.enabled:
        _disable_remaining_instances(instance)


def _disable_remaining_instances(instance) -> None:
    instance.__class__.objects.exclude(pk=instance.pk).update(enabled=False)

