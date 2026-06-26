import pickle

from document_summary_agent import (
    summarize_document
)

with open(
    "documents.pkl",
    "rb"
) as f:

    documents = pickle.load(
        f
    )

summary = summarize_document(
    documents
)

print(
    "\nSUMMARY:\n"
)

print(
    summary
)