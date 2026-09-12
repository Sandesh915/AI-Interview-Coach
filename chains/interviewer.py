from langchain_openrouter import ChatOpenRouter
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)


INTERVIEWER_SYSTEM_PROMPT = """
You are an expert technical interviewer.

Your role:
- Ask one clear, focused question at a time.
- Reference previous answers when relevant.
- Build on the conversation naturally.
- Avoid repeating questions.
- Be professional but encouraging.

Interview type: {interview_type}
Position level: {level}
Focus area: {focus_area}

Use the conversation history to understand what has already
been discussed.
"""


# Store conversation histories for different interview sessions
session_store: dict[str, InMemoryChatMessageHistory] = {}


def get_session_history(
    session_id: str,
) -> BaseChatMessageHistory:

    if session_id not in session_store:
        session_store[session_id] = InMemoryChatMessageHistory()

    return session_store[session_id]


def create_interviewer_with_history():
    """Create an interviewer chain with conversation history."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", INTERVIEWER_SYSTEM_PROMPT),

        MessagesPlaceholder(
            variable_name="history"
        ),

        ("human", "{input}"),
    ])

    llm = ChatOpenRouter(
        model="openai/gpt-chat-latest",
        temperature=0.7,
        max_tokens=512,
    )

    chain = prompt | llm | StrOutputParser()

    chain_with_history = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )

    return chain_with_history