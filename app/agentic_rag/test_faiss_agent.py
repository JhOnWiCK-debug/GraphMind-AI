from retrieval.faiss_store import FAISSStore
from retrieval.faiss_retriever import FAISSRetriever

from faiss_agent import (
    faiss_agent
)

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

    answer = faiss_agent(
        question,
        retriever
    )

    print(
        "\nAnswer:\n"
    )

    print(
        answer
    )