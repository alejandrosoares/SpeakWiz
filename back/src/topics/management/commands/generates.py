from django.core.management.base import BaseCommand

from services.topics.generate.main import TopicGenerator


class Command(BaseCommand):

    def handle(self, *args, **options):
        topic_generator = TopicGenerator()
        topic_generator.start()


