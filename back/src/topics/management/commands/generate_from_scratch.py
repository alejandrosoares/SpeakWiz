from django.core.management.base import BaseCommand

from services.topics.generate.main import TopicGeneratorFromScratch


class Command(BaseCommand):

    def handle(self, *args, **options):
        topic_generator = TopicGeneratorFromScratch()
        topic_generator.start()


