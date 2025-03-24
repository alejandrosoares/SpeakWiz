from .models import Language


def get_default_language() -> Language:
    return Language.objects.get(code='en')