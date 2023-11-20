from django.conf import settings

import openai
from langchain.llms import OpenAI

# Change OpenAI for
# from langchain.chat_models import ChatOpenAI`


openai.api_key = settings.OPENAI_API_KEY


class LLModelSingleton:
    temperature = 0.0
    model_name="gpt-3.5-turbo"
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = OpenAI(temperature=cls.temperature, model_name=cls.model_name)
        return cls.__instance