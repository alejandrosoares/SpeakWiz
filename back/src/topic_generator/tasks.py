from main.celery import app
from .models import GenerationSettings
from .implementations import generate_new_topic_from_random_topictag


if GenerationSettings.objects.first().enabled:
    every_hour = 60 * 60

    @app.task
    def generate_new_topic_task():
        generate_new_topic_from_random_topictag()

    app.add_periodic_task(
        every_hour,
        generate_new_topic_task, 
        name='generate_new_topic_task_hourly'
    )