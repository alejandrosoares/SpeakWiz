from django.apps import AppConfig


class TopicGeneratorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'topic_generator'

    def ready(self):
        import topic_generator.signals
