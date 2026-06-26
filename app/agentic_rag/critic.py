from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3:8b"
)

def evaluate_answer(
    question,
    context,
    answer
):

    prompt = f"""
Question:
{question}

Context:
{context}

Answer:
{answer}

Is the answer fully supported by the context?

Reply only:
YES
or
NO
"""

    response = llm.invoke(
        prompt
    )

    return response.content