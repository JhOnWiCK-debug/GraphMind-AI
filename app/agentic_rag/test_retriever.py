from faiss_indexer import FAISSIndexer
from retrieval.faiss_retriever import FAISSRetriever

chunks = [
    "Super Saturday is a shopping event.",
    "Python is a programming language.",
    "GraphRAG combines graphs and retrieval."
]

indexer = FAISSIndexer()

store = indexer.index_documents(
    chunks
)

retriever = FAISSRetriever(
    store
)

results = retriever.retrieve(
    "What is Super Saturday?"
)

print(results)