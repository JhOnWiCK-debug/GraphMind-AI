from sentence_transformers import SentenceTransformer

from retrieval.faiss_store import FAISSStore


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

docs = [
    "Super Saturday is a shopping event.",
    "Python is a programming language.",
    "GraphRAG combines graphs and retrieval."
]

embeddings = model.encode(
    docs
)

dimension = len(
    embeddings[0]
)

store = FAISSStore(
    dimension
)

store.add_documents(
    embeddings,
    docs
)

query = "What is Super Saturday?"

query_embedding = model.encode(
    query
)

results = store.search(
    query_embedding,
    k=2
)

print(results)