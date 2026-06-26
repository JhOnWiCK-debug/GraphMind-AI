from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3:8b"
)


def extract_relationships(text):

    prompt = f"""
Extract relationships from the text.

IMPORTANT:
Return ONLY a Python list.

DO NOT explain.
DO NOT add notes.
DO NOT add headings.

Correct format:

[
("Wheelz","imports_from","China"),
("India","currency","INR")
]

Text:
{text[:3000]}
"""

    response = llm.invoke(
        prompt
    )

    return response.content