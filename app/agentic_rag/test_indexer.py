from faiss_indexer import FAISSIndexer

chunks = [
    "Super Saturday is a shopping event.",
    "Python is a programming language.",
    "GraphRAG combines graphs and retrieval."
]

indexer = FAISSIndexer()

store = indexer.index_documents(
    chunks
)

print(
    "Indexed:",
    len(chunks),
    "documents"
)