from enum import Enum

from topics.models import Topic
from .models import UserPreference


ENABLED_MODELS = {
    'topic': Topic
}


class Feedback(Enum):
    LIKE = 1
    DISLIKE = 2
    REMOVE = 3

    @classmethod
    def validate_value(cls, value):
        valid_values = (cls.LIKE.value, cls.DISLIKE.value, cls.REMOVE.value)
        return value in valid_values


def get_enabled_model_from(resource_type):
    return ENABLED_MODELS.get(resource_type)


def update_user_preference(resource, feedback, user):
    if Feedback.validate_value(feedback):
        user_preference, _ = UserPreference.objects.get_or_create(user=user)
        resource_model = resource.__class__.__name__.lower()
        preferences = user_preference.preferences
        resource_preference = preferences.get(resource_model, {})
        resource_preference[str(resource.id)] = feedback
        preferences[resource_model] = resource_preference
        user_preference.preferences = preferences
        user_preference.save()
