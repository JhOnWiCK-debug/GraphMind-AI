from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3:8b"
)


def summarize_document(
    documents
):

    text = "\n".join(
        documents[:20]
    )

    prompt = f"""
Summarize this document.

Include:

1. Main topic
2. Purpose
3. Key sections

Document:

{text}
"""

    response = llm.invoke(
        prompt
    )

    return response.content