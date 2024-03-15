from langchain.prompts import ChatPromptTemplate


_TEMPLATE = """
Giving the following text in {original_language} translate it to {target_language}:

{topic}

<<OUTPUT_FORMAT>>
The output must be formatted as a JSON instance that conforms to the JSON schema below:
{{
    "title": "Here put the translated title",
    "description": "Here put the translated description",
    "questions": [
        "Here write the translation of question 1",
        "Here write the translation of question 2",
        "Here write the translation of question 3",
        "Here write the translation of question 4",
        "Here write the translation of question 5",
        "Here write the translation of question 6",
        "Here write the translation of question 7",
        "Here write the translation of question 8",
        "Here write the translation of question 9",
        "Here write the translation of question 10",
    ]
}}
You must respond ONLY THE JSON STRUCTURE, NOTHING MORE.
"""

def get_prompt_template() -> ChatPromptTemplate:
    return ChatPromptTemplate.from_template(_TEMPLATE)