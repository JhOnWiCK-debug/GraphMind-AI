from pdf_processor import extract_text
from text_chunker import chunk_text
from retrieval.embed_chunks import embed_chunks

from retrieval.faiss_store import FAISSStore


def add_pdf_to_faiss(
    pdf_path
):

    text = extract_text(
        pdf_path
    )

    chunks = chunk_text(
        text
    )

    embeddings = embed_chunks(
        chunks
    )

    store = FAISSStore.load(
        "faiss.index",
        "documents.pkl"
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
        f"Added {len(chunks)} chunks"
    )