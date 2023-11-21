from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import TopicTag


@receiver(m2m_changed, sender=TopicTag.topics.through)
def m2m_changed_topic_tags(sender, instance, action, **kwargs):
    number_topics_changed = kwargs.get('pk_set')
    if action == "post_add":
        instance.number_topics += len(number_topics_changed) 
    elif action == "post_remove":
        instance.number_topics -= len(number_topics_changed)
    instance.save()