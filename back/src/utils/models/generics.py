from django.contrib.contenttypes.models import ContentType

from topics.models import Topic
from topics.serializers import TopicListSerializer


ENABLED_RESOURCE_MODELS = {
    'topic': {
        'model': Topic,
        'serializer': TopicListSerializer
    }

}


def get_generic_enabled_model(resource_type):
    return ENABLED_RESOURCE_MODELS.get(resource_type).get('model')


def get_content_type_model(resource_type):
    Model = get_generic_enabled_model(resource_type)
    model_type = ContentType.objects.get_for_model(Model)
    return model_type
