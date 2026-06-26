import faiss
import numpy as np
import pickle


class FAISSStore:

    def __init__(self, dimension):

        self.index = faiss.IndexFlatL2(
            dimension
        )

        self.documents = []

    def add_documents(
        self,
        embeddings,
        documents
    ):

        embeddings = np.array(
            embeddings
        ).astype(
            "float32"
        )

        self.index.add(
            embeddings
        )

        self.documents.extend(
            documents
        )

    def search(
        self,
        query_embedding,
        k=3
    ):

        query_embedding = np.array(
            [query_embedding]
        ).astype(
            "float32"
        )

        distances, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for idx in indices[0]:

            if idx < len(
                self.documents
            ):
                results.append(
                    self.documents[idx]
                )

        return results

    def save(
        self,
        index_path,
        docs_path
    ):

        faiss.write_index(
            self.index,
            index_path
        )

        with open(
            docs_path,
            "wb"
        ) as f:

            pickle.dump(
                self.documents,
                f
            )

    @classmethod
    def load(
        cls,
        index_path,
        docs_path
    ):

        index = faiss.read_index(
            index_path
        )

        with open(
            docs_path,
            "rb"
        ) as f:

            documents = pickle.load(
                f
            )

        obj = cls(
            index.d
        )

        obj.index = index

        obj.documents = documents

        return obj