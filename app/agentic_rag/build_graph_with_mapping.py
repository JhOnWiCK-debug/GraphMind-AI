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

chunk_to_node = {}

for i, chunk in enumerate(
    all_chunks
):
    chunk_to_node[chunk] = i

with open(
    "graph.pkl",
    "wb"
) as f:

    pickle.dump(
        graph,
        f
    )

with open(
    "chunk_mapping.pkl",
    "wb"
) as f:

    pickle.dump(
        chunk_to_node,
        f
    )

print(
    f"Graph Saved: {graph.number_of_nodes()} nodes"
)

print(
    f"Mapping Saved: {len(chunk_to_node)} chunks"
)