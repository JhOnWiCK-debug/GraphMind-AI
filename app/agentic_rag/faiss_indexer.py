from sentence_transformers import SentenceTransformer
from retrieval.faiss_store import FAISSStore


class FAISSIndexer:

    def __init__(self):

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        self.store = None

    def index_documents(
        self,
        chunks
    ):

        embeddings = self.model.encode(
            chunks
        )

        dimension = len(
            embeddings[0]
        )

        self.store = FAISSStore(
            dimension
        )

        self.store.add_documents(
            embeddings,
            chunks
        )

        return self.store