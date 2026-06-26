from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3:8b"
)

def rewrite_query(question):

    prompt = f"""
You are a search query optimizer.

Rewrite the question to improve retrieval.

Rules:
- Return ONLY the rewritten question.
- No explanations.
- No quotes.
- One sentence only.

Question:
{question}
"""

    response = llm.invoke(
        prompt
    )

    return response.content.strip()