from graph_builder import build_graph
from graph.graph_retriever

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

result = graph_search(
    graph,
    start_node=2,
    depth=1
)

print(result)