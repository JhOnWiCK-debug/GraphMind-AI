from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3:8b"
)

def extract_entities(text):

    prompt = f"""
Extract important entities from the text.

Return ONLY a Python list.

Example:
["Vishva", "Saveetha University", "Python"]

Text:
{text[:2000]}
"""

    response = llm.invoke(
        prompt
    )

    return response.content