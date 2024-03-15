from topics.models import Topic


def get_topic_as_text(topic:Topic) -> str:
    questions = topic.get_list_questions()
    title = f'Title: {topic.title}\n'
    description = f'Description: {topic.description}\n'
    str_questions = 'Questions:\n-' + '\n-'.join(q for q in questions)
    return ''.join([title, description, str_questions])