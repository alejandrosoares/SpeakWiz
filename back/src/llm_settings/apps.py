from django.apps import AppConfig


class LlmSettingsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'llm_settings'

    def ready(self):
        import llm_settings.signals