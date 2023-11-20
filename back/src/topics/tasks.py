from main.celery import app
from services.topics.generate import TopicGeneratorFromExisting, TopicGeneratorFromScratch


every_five_minute_schedule = 60 * 5


@app.task
def generate_topics_from_existing():
    topic_generator = TopicGeneratorFromExisting()
    topic_generator.start()


@app.task
def generate_topics_from_scratch():
    topic_generator = TopicGeneratorFromScratch()
    topic_generator.start()


app.add_periodic_task(
    every_five_minute_schedule,
    generate_topics_from_existing, 
    name='generate-topics-from-existing-five-min'
)


app.add_periodic_task(
    every_five_minute_schedule,
    generate_topics_from_scratch, 
    name='generate-topics-from-scratch-five-min'
)