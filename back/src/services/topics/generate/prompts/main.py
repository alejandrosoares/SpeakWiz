from langchain.prompts import PromptTemplate


__CONTEXT = """
<<CONTEXT>>
I am practicing speaking in English by using cards of different topics.
"""


__OUTPUT_FORMAT = """
<<OUTPUT FORMAT>>
The output must be formatted as a JSON instance that conforms to the JSON schema below:
{{
    "title": "Here put the title",
    "description": "Here put an elegant short description of what about the questions are to show all the users who want to use this card",
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



TEMPLATE = f"""
    {__CONTEXT}

    {__OUTPUT_FORMAT}

    {{instruction}}

    {{input_context}}
"""


class TopicPromptSingleton:
    __instance = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = PromptTemplate(
                template=TEMPLATE, 
                input_variables=[
                    "instruction",
                    "input_context",
                    ]
                )
        return cls.__instance
