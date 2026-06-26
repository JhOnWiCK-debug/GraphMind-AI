import pickle
from retrieval.faiss_store import FAISSStore
from retrieval.faiss_retriever import FAISSRetriever

from graph.graph_retriever

from langchain_ollama import ChatOllama

from critic import evaluate_answer
from query_rewriter import rewrite_query


# -------------------
# LOAD FAISS
# -------------------

store = FAISSStore.load(
    "faiss.index",
    "documents.pkl"
)

retriever = FAISSRetriever(
    store
)


# -------------------
# LOAD GRAPH
# -------------------

with open(
    "graph.pkl",
    "rb"
) as f:

    graph = pickle.load(
        f
    )

with open(
    "chunk_mapping.pkl",
    "rb"
) as f:

    chunk_mapping = pickle.load(
        f
    )

# -------------------
# LLM
# -------------------

llm = ChatOllama(
    model="llama3:8b"
)


# -------------------
# RETRIEVE
# -------------------

def retrieve_context(question):

    results = retriever.retrieve(
        question,
        k=3
    )

    expanded_chunks = []

    for chunk in results:

        expanded_chunks.append(
            chunk
        )

        if chunk in chunk_mapping:

            node_id = chunk_mapping[
                chunk
            ]

            neighbors = graph_search(
                graph,
                node_id,
                depth=1
            )

            for neighbor in neighbors:

                neighbor_text = graph.nodes[
                    neighbor
                ]["text"]

                expanded_chunks.append(
                    neighbor_text
                )

    expanded_chunks = list(
        dict.fromkeys(
            expanded_chunks
        )
    )

    context = "\n".join(
        expanded_chunks
    )

    return context

# -------------------
# GENERATE
# -------------------

def generate_answer(
    question,
    context
):

    prompt = f"""
You are a document assistant.

Rules:
1. Answer ONLY from the provided context.
2. If the answer is not present in the context, reply exactly:
I could not find that information in the uploaded documents.
3. Do not use outside knowledge.
4. Keep answers concise.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(
        prompt
    )

    return response.content


# -------------------
# MAIN LOOP
# -------------------

question = input(
    "\nAsk a Question: "
)

attempts = 0

while attempts < 3:

    print(
        f"\nAttempt {attempts + 1}"
    )

    context = retrieve_context(
        question
    )

    print(
    f"\nContext Length: {len(context)}"
)

    answer = generate_answer(
        question,
        context
    )

    verdict = evaluate_answer(
        question,
        context,
        answer
    )

    print(
        f"\nCritic Verdict: {verdict}"
    )

    if "YES" in verdict.upper():

        print(
            "\nFINAL ANSWER:\n"
        )

        print(answer)

        break

    question = rewrite_query(
        question
    )

    print(
        f"\nRewritten Query: {question}"
    )

    attempts += 1


if attempts == 3:

    print(
        "\nFINAL ANSWER:\n"
    )

    print(answer)