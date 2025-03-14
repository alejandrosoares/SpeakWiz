from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver

from topic_generator.implementations import translate_topic
from .models import Topic


@receiver(pre_save, sender=Topic)
def pre_save_topic(sender, instance, **kwargs):
    try:
        previous_instance = sender.objects.get(pk=instance.pk)
    except Topic.DoesNotExist:
        previous_instance = None
    else:
        is_enabled = not previous_instance.is_enabled and instance.is_enabled
        is_root = instance.reference is None
        was_not_translated = sender.objects.filter(reference=instance).count() == 0
        is_translatable = is_enabled and is_root and was_not_translated
        if is_translatable:
            translate_topic(instance)

        
@receiver(post_save, sender=Topic)
def post_save_topic(sender, instance, created, **kwargs):
    if created:
        instance.tag.increase_number_topics()


@receiver(post_delete, sender=Topic)
def post_delete_topic(sender, instance, **kwargs):
    instance.tag.decrease_number_topics()
