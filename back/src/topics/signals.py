from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from services.topics.translation import TopicTranslator
from .models import TopicTranslation, TopicTag


@receiver(m2m_changed, sender=TopicTag.topics.through)
def m2m_changed_topic_tags(sender, instance, action, **kwargs):
    number_topics_changed = kwargs.get('pk_set')
    if action == "post_add":
        instance.number_topics += len(number_topics_changed) 
    elif action == "post_remove":
        instance.number_topics -= len(number_topics_changed)
    instance.save()


@receiver(m2m_changed, sender=TopicTranslation.languages.through)
def m2m_changed_topic_translation(sender, instance, action, **kwargs):
    if action == "post_add":
        for lang in instance.languages.all():
            translator = TopicTranslator(instance.topic, lang)
            translator.translate_and_save()