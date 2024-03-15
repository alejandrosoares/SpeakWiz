from typing import List

from langchain.pydantic_v1 import BaseModel, Field


class TopicOutput(BaseModel):
    title: str = Field(description="title of the new topic")
    description: str = Field(description="Description of what about the questions are")
    questions: List[str] = Field(description="list of questions of this topic")