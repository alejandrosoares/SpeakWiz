from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=12, unique=True)

    @staticmethod
    def get_lang_name_by_code(code: str) -> str:
        return Language.objects.get(code=code).name

    def __str__(self):
        return self.code
