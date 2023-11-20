from abc import ABC, abstractmethod

from topics.models import Topic, TopicTag


class ITopicFormatter(ABC):

    @abstractmethod
    def get_input_context(self) -> str:
        pass


class TopicFormatter(ITopicFormatter):
    topic_separator = '\n\n' 
    line_separator = '\n'

    def __init__(self, tag: TopicTag, topics: Topic) -> None:
        self.topics = topics
        self.tag = tag
        self.cls = TopicFormatter
    
    def get_input_context(self) -> str:
        topics_list = tuple(self.__generate_topic_text(topic, index) for index, topic in enumerate(self.topics, start=1))
        result_list = [
            self.__get_current_topic_title(),
            self.__get_examples_title()
        ]
        result_list.extend(topics_list)
        return self.cls.line_separator.join(result_list)

    def __get_current_topic_title(self) -> str:
        return f'The CURRENT topic is {self.tag.tag.upper()}'
    
    def __get_examples_title(self) -> str:
        return f'The examples are:'

    def __generate_topic_text(self, topic, index) -> str:
        example_title = self.__format_row('card example', index)
        title = self.__format_row('title', topic.title)
        description = self.__format_row('description', topic.description)
        questions = self.__get_questions_as_text(topic)
        topic_text = self.cls.line_separator.join((example_title, title, description, questions))
        return f'{topic_text}{self.cls.topic_separator}'

    def __format_row(self, key, value):
        return f'{key}: {value}'
    
    def __get_questions_as_text(self, topic) -> str:
        questions = (card.question  for card in topic.cards.all())
        return self.line_separator.join(questions)


class TagFormatter(ITopicFormatter):

    def __init__(self, tag: TopicTag) -> None:
        self.tag = tag

    def get_input_context(self) -> str:
        return self.__get_current_topic_title()

    def __get_current_topic_title(self) -> str:
        return f'The CURRENT topic is {self.tag.tag.upper()}'
