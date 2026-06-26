import chromadb

client = chromadb.PersistentClient(
    path="./vector_store"
)

print(
    client.list_collections()
)