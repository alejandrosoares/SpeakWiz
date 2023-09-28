from main.celery import app
from services.topics.generate.main import TopicGenerator


every_five_minute_schedule = 60 * 5

@app.task
def generate_topics_task():
    topic_generator = TopicGenerator()
    topic_generator.start()


app.add_periodic_task(60 * 5, generate_topics_task, name='generate-topics-task-five-min')