from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3:8b"
)


def understand_question(
    question,
    graph
):

    relations = set()

    for _, _, data in graph.edges(
        data=True
    ):

        relations.add(
            data["relation"]
        )

    relation_list = list(
        relations
    )

    prompt = f"""
You are a graph query translator.

Available relations:

{relation_list}

CRITICAL RULES:

Return ONLY ONE LINE.

Format:

entity|relation

DO NOT explain.
DO NOT add labels.
DO NOT add notes.
DO NOT add examples.
DO NOT add markdown.

Correct:

Wheelz|imports_from

Correct:

Wheelz|produces_in

Wrong:

Entity: Wheelz
Relation: produces_in

Wrong:

Easy one!
Wheelz|produces_in

Question:

{question}
"""

    response = llm.invoke(
        prompt
    )

    return response.content.strip()