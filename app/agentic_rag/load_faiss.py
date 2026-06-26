from retrieval.faiss_store import FAISSStore
from retrieval.faiss_retriever import FAISSRetriever

store = FAISSStore.load(
    "faiss.index",
    "documents.pkl"
)

retriever = FAISSRetriever(
    store
)

question = input(
    "Ask: "
)

results = retriever.retrieve(
    question
)

print("\nRESULTS:\n")

for r in results:

    print("-" * 50)
    print(r)