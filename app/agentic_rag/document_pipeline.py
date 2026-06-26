from pdf_processor import extract_text

from text_chunker import chunk_text

from retrieval.embed_chunks import embed_chunks

from retrieval.faiss_store import FAISSStore

from relationship_extractor import (
    extract_relationships
)

from graph.build_knowledge_graph import (
    build_knowledge_graph
)

import pickle
import ast


def process_document(
    pdf_path
):

    print("\n[1] Extracting Text...")

    text = extract_text(
        pdf_path
    )

    print(
        f"Characters: {len(text)}"
    )

    print("\n[2] Chunking...")

    chunks = chunk_text(
        text
    )

    print(
        f"Chunks: {len(chunks)}"
    )

    print("\n[3] Creating Embeddings...")

    embeddings = embed_chunks(
    chunks
    )

    print(
        f"Embeddings: {len(embeddings)}"
    )

    print("\n[4] Building FAISS...")

    store = FAISSStore(
        len(
            embeddings[0]
        )
    )

    store.add_documents(
        embeddings,
        chunks
    )

    store.save(
        "faiss.index",
        "documents.pkl"
    )

    print(
        "FAISS Saved"
    )

    print("\n[5] Extracting Relationships...")

    raw_relationships = (
        extract_relationships(
            text
        )
    )
    print("\nRAW RELATIONSHIPS:\n")
    print(raw_relationships)

    try:

        relationships = ast.literal_eval(
            raw_relationships
        )

        print("\nPARSED RELATIONSHIPS:\n")
        print(relationships)

    except Exception:

        print(
            "\nCould not parse relationships."
        )

        relationships = []

    print(
        f"Relationships: {len(relationships)}"
    )

    print("\n[6] Building Knowledge Graph...")

    graph = build_knowledge_graph(
        relationships
    )

    with open(
        "knowledge_graph.pkl",
        "wb"
    ) as f:

        pickle.dump(
            graph,
            f
        )

    print(
        "Knowledge Graph Saved"
    )

    print(
        "\nPipeline Complete"
    )