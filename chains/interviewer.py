from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


INTERVIEWER_STYLES = {
    "friendly": (
        "Be warm and encouraging. Help the candidate feel comfortable."
    ),
    "challenging": (
        "Push back on answers. Ask follow-up questions and test depth."
    ),
    "neutral": (
        "Be professional and straightforward. Give minimal feedback."
    ),
}


INTERVIEWER_SYSTEM_PROMPT = """
You are an expert technical interviewer conducting a {interview_type} interview.

Your role:
- Ask one clear, focused question at a time.
- Questions should be appropriate for a {level} position.
- Be professional and encouraging.
- After the candidate answers, provide brief acknowledgment before asking the next question.

Interview focus:
{focus_area}

Interviewer style:
{interviewer_style}

Current question number:
{question_number} of {total_questions}
"""


interviewer_prompt = ChatPromptTemplate.from_messages([
    ("system", INTERVIEWER_SYSTEM_PROMPT),

    MessagesPlaceholder(
        variable_name="history",
        optional=True
    ),

    ("human", "{input}")
])


def create_interviewer_chain(
    model: str = "gpt-4o-mini",
    temperature: float = 0.7,
):
    llm = ChatOpenAI(
        model=model,
        temperature=temperature,
    )

    chain = interviewer_prompt | llm | StrOutputParser()

    return chain