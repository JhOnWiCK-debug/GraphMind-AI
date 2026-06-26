import pickle

from document_loader import load_documents
from graph_builder import build_graph

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

graph = build_graph(
    all_chunks
)

with open(
    "graph.pkl",
    "wb"
) as f:

    pickle.dump(
        graph,
        f
    )

print(
    f"Graph Saved: {graph.number_of_nodes()} nodes"
)