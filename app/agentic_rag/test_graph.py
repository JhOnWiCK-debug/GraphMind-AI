from graph_builder import build_graph

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

print(
    "Nodes:",
    graph.number_of_nodes()
)

print(
    "Edges:",
    graph.number_of_edges()
)

print(
    list(graph.neighbors(2))
)