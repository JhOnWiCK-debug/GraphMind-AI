from graph_builder import build_graph
from hybrid_retriever import hybrid_retrieve

chunks = [
    "Data Science",
    "Machine Learning",
    "Neural Networks",
    "Transformers",
    "GraphRAG"
]

graph = build_graph(
    chunks
)

vector_results = [2]

result = hybrid_retrieve(
    graph,
    vector_results
)

print(result)