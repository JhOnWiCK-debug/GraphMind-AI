from document_loader import load_documents

docs = load_documents(
    "data/docs"
)

print(
    f"Loaded {len(docs)} PDFs"
)

print(
    docs[0]["filename"]
)