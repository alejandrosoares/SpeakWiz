"""
It validates if the new content meets the requirements to be enabled automatically
Requirements:
1) Does not have many repeated questions. It is defined by a score and compared with a threshold
How is the score calculated?
repeated_ratio = <repeated_questions> / <number_topics>
score = (<number_questions>  - <repeated_ratio>) / <number_questions>
"""

from typing import List

from topics.models import Topic
from .parsers import TopicOutput


class TopicGeneratorValidator:

    threshold = 0.8

    def __init__(self, topics: List[Topic], topic_output: TopicOutput) -> None:
        self.topics = topics
        self.topic_output = topic_output
        self.number_topics = len(topics)
        self.repeated = 0
        self.cls = TopicGeneratorValidator

    def validate(self) -> bool:
        repeated_ratio = self.__get_repeated_ratio()
        score = (self.number_topics - repeated_ratio) / self.number_topics
        return score >= self.cls.threshold
    
    def __get_repeated_ratio(self) -> float:
        new_questions = set(self.topic_output.questions)
        for topic in self.topics:
            questions = set(topic.get_list_questions())
            self.repeated += len(new_questions & questions)
        return self.repeated / self.number_topics
        
