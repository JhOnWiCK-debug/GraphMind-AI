from document_loader import load_documents

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

print(
    f"Loaded {len(docs)} PDFs"
)

print(
    f"Created {len(all_chunks)} chunks"
)