from sentence_transformers import SentenceTransformer


class FAISSRetriever:

    def __init__(
        self,
        store
    ):

        self.store = store

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    def retrieve(
        self,
        question,
        k=3
    ):

        query_embedding = self.model.encode(
            question
        )

        results = self.store.search(
            query_embedding,
            k
        )

        return results