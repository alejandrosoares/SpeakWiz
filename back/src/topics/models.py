from django.db import models

from languages.models import Language


class Topic(models.Model):
    reference = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, blank=True, 
        related_name='translations'
    )
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    premium = models.BooleanField(default=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    autogenerated = models.BooleanField(default=False)

    @staticmethod
    def create(title, description, lang, reference, enabled = True, autogenerated = False):
        topic = Topic.objects.create( 
            title=title,
            description=description,
            lang=lang,
            enabled=enabled,
            autogenerated=autogenerated,
            reference=reference
        )
        return topic
    
    def get_list_questions(self) -> tuple[str]:
        questions = (card.question for card in self.cards.all())
        return questions
    
    def get_lang_name(self) -> str:
        return self.lang.name

    def __str__(self):
        return f'{self.title} {self.id}'


class TopicTag(models.Model):
    tag = models.CharField(max_length=50)
    topics = models.ManyToManyField(Topic, blank=True)
    number_topics = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.tag
    

class TopicTranslation(models.Model):
    topic = models.OneToOneField(Topic, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return f'{self.topic.title} {self.id}'