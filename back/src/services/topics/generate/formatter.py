from topics.models import Topic, TopicTag


class TopicFormatter:
    TOPIC_SEPARATOR = '\n\n' 
    LINE_SEPARATOR = '\n'

    def __init__(self, topics: Topic, tag: TopicTag) -> None:
        self.topics = topics
        self.tag = tag
        self.cls = TopicFormatter
    
    def get_formatted_text(self) -> str:
        topics_list = tuple(self.__generate_topic_text(topic, index) for index, topic in enumerate(self.topics, start=1))
        result_list = [
            self.__get_current_topic_title(self.tag),
            self.__get_examples_title()
        ]
        result_list.extend(topics_list)
        return self.cls.LINE_SEPARATOR.join(result_list)

    def __get_current_topic_title(self, tag: TopicTag) -> str:
        return f'The CURRENT topic is {tag.tag.upper()}'
    
    def __get_examples_title(self) -> str:
        return f'The examples are:'

    def __generate_topic_text(self, topic, index) -> str:
        example_title = self.__format_row('card example', index)
        title = self.__format_row('title', topic.title)
        description = self.__format_row('description', topic.description)
        questions = self.__get_questions_as_text(topic)
        topic_text = self.cls.LINE_SEPARATOR.join((example_title, title, description, questions))
        return f'{topic_text}{self.cls.TOPIC_SEPARATOR}'

    def __format_row(self, key, value):
        return f'{key}: {value}'
    
    def __get_questions_as_text(self, topic) -> str:
        questions = (card.question  for card in topic.cards.all())
        return self.LINE_SEPARATOR.join(questions)
