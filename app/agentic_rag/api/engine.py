import pickle

from ..retrieval.faiss_store import FAISSStore
from ..retrieval.faiss_retriever import FAISSRetriever

class GraphMindEngine:

    def __init__(self):

        with open(
            "knowledge_graph.pkl",
            "rb"
        ) as f:

            self.graph = pickle.load(f)

        with open(
            "documents.pkl",
            "rb"
        ) as f:

            self.documents = pickle.load(f)

        store = FAISSStore.load(
            "faiss.index",
            "documents.pkl"
        )

        self.retriever = FAISSRetriever(
            store
        )


engine = GraphMindEngine()