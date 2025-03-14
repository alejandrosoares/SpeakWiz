"""
This module contains the implementation of the models from different providers.

Classes:
    LLMModelFactory: A factory class to get instances of language models.
Functions:
    LLMModelFactory.get_model(model: 'llm_settings.models.LLMModel') -> Any:
        Get the chat model instance based on the model name and temperature.
Constants:
    AVAILABLE_LLM_MODELS: A list of available language models from different providers.
"""

from typing import Any
import os
import openai
from langchain_openai import ChatOpenAI


AVAILABLE_LLM_MODELS = []


_OPEN_AI_MODELS = [
    "gpt-3.5-turbo",
    "text-davinci-003",
    "text-davinci-002",
    "text-curie-001",
    "text-babbage-001",
    "text-ada-001",
    "gpt-4",
    "gpt-4-turbo",
]


AVAILABLE_LLM_MODELS += _OPEN_AI_MODELS


class LLMModelFactory:

    @classmethod
    def get_model(cls, model: "llm_settings.models.LLMModel") -> ChatOpenAI:
        """Get the chat model instance"""
        if model.name in _OPEN_AI_MODELS:
            return cls._get_open_ai_model(model.name, model.temperature)
        raise ValueError(f"Model {model.name} not available")

    def _get_open_ai_model(model_name, temperature) -> ChatOpenAI:
        OPENAI_KEY = os.getenv("OPENAI_API_KEY", "invalid-key")
        openai.api_key = OPENAI_KEY
        return ChatOpenAI(model=model_name, temperature=temperature)
