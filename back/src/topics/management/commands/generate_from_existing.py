from django.core.management.base import BaseCommand

from services.topics.generate.main import TopicGeneratorFromExisting


class Command(BaseCommand):

    def handle(self, *args, **options):
        topic_generator = TopicGeneratorFromExisting()
        topic_generator.start()


