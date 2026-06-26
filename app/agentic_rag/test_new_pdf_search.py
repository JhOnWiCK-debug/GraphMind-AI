from retrieval.faiss_store import FAISSStore
from retrieval.faiss_retriever import FAISSRetriever

store = FAISSStore.load(
    "faiss.index",
    "documents.pkl"
)

retriever = FAISSRetriever(
    store
)

results = retriever.retrieve(
    "Wheelz car manufacturing company",
    k=3
)

for r in results:

    print(
        "\n-----------------\n"
    )

    print(r)