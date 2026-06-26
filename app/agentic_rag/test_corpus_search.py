from document_loader import load_documents
from faiss_indexer import FAISSIndexer
from retrieval.faiss_retriever import FAISSRetriever

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

docs = load_documents(
    "data/docs"
)

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

all_chunks = []

for doc in docs:

    chunks = splitter.split_text(
        doc["text"]
    )

    all_chunks.extend(
        chunks
    )

indexer = FAISSIndexer()

store = indexer.index_documents(
    all_chunks
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