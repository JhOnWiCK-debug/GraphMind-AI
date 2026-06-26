from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3:8b"
)


def parse_question(
    question
):

    prompt = f"""
Extract:

1. entity
2. relation

Return ONLY:

entity|relation

Examples:

What currency does India use?

India|currency

Where does Wheelz import from?

Wheelz|imports_from

Question:

{question}
"""

    response = llm.invoke(
        prompt
    )

    return response.content.strip()