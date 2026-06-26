import chromadb

from sentence_transformers import SentenceTransformer


def store_chunks(chunks):

    model = SentenceTransformer(
        "sentence-transformers/all-MiniLM-L6-v2"
    )

    client = chromadb.PersistentClient(
        path="./vector_store"
    )

    try:
        client.delete_collection(
            "documents"
        )
    except:
        pass

    collection = client.create_collection(
        "documents"
    )

    embeddings = model.encode(
        chunks
    ).tolist()

    ids = [
        f"chunk_{i}"
        for i in range(len(chunks))
    ]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )

    return len(chunks)