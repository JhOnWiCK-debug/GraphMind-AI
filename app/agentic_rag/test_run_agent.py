import pickle

from retrieval.faiss_store import FAISSStore
from retrieval.faiss_retriever import FAISSRetriever
from run_agent import (
    run_agent
)

with open(
    "documents.pkl",
    "rb"
) as f:
    documents = pickle.load(f)

store = FAISSStore.load(
    "faiss.index",
    "documents.pkl"
)

print("Creating retriever...")

retriever = FAISSRetriever(store)

print("Retriever created successfully!")

# Knowledge Graph

with open(
    "knowledge_graph.pkl",
    "rb"
) as f:

    graph = pickle.load(
        f
    )

# Documents

with open(
    "documents.pkl",
    "rb"
) as f:

    documents = pickle.load(
        f
    )

# FAISS

store = FAISSStore.load(
    "faiss.index",
    "documents.pkl"
)

retriever = FAISSRetriever(
    store
)

while True:

    question = input(
        "\nQuestion: "
    )

    answer = run_agent(
        question,
        graph,
        retriever,
        documents
    )

    print(
        "\nAnswer:\n"
    )

    print(
        answer
    )