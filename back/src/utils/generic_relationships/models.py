from django.contrib.contenttypes.models import ContentType

from topics.models import Topic
from topics.serializers import TopicListSerializer


ENABLED_RESOURCE_MODELS = {
    'topic': {
        'model': Topic,
        'serializer': TopicListSerializer
    }

}