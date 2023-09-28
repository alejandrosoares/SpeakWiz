from langchain.prompts import PromptTemplate


__CONTEXT = """
I am practicing speaking in English by using cards of different topics.
"""


__OUTPUT_FORMAT = """
<<OUTPUT FORMAT>>
The output must be formatted as a JSON instance that conforms to the JSON schema below:
{{
    "title": "Here put the title",
    "description": "Here put a short description of what about the questions are",
    "questions": [
        "Here write the question 1",
        "Here write the question 2",
        "Here write the question 3",
        "Here write the question 4",
        "Here write the question 5",
        "Here write the question 6",
        "Here write the question 7",
        "Here write the question 8",
        "Here write the question 9",
        "Here write the question 10",
    ]
}}
You must respond ONLY THE JSON STRUCTURE, NOTHING MORE.
"""


__INSTRUCTION = """
<<INSTRUCTION>>
Please take these examples and give ANOTHER card more about the CURRENT TOPIC, 
but with a DIFFERENT TITLE (2 words at least), a DIFFERENT DESCRIPTION and others 10 DIFFERENT QUESTIONS to the examples.
The new card must the DIFFERENT to the given examples but it must be related to the SAME TOPIC.
"""


TEMPLATE = f"""
{__CONTEXT}

{__OUTPUT_FORMAT}

{__INSTRUCTION}

{{topics_text}}"""


class TopicPromptSingleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = PromptTemplate(
                template=TEMPLATE, 
                input_variables=[
                    "topics_text",
                    ]
                )
        return cls.__instance
