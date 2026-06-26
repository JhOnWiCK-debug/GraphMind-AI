from graph_facts import (
    get_graph_facts
)

from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="llama3:8b"
)


def hybrid_agent(
    question,
    knowledge_graph,
    retriever
):

    graph_facts = get_graph_facts(
        knowledge_graph
    )

    chunks = retriever.retrieve(
        question,
        k=3
    )

    context = "\n\n".join(
        chunks
    )

    prompt = f"""
Answer using:

1. Graph Facts
2. Retrieved Context

Graph Facts:

{graph_facts}

Retrieved Context:

{context}

Question:

{question}

Think step-by-step.

Return only the answer.
"""

    response = llm.invoke(
        prompt
    )

    return response.content