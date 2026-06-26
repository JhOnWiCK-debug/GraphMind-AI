import pickle

from graph_retriever import graph_search

with open(
    "graph.pkl",
    "rb"
) as f:

    graph = pickle.load(
        f
    )

print(
    f"Nodes: {graph.number_of_nodes()}"
)

results = graph_search(
    graph,
    start_node=10,
    depth=1
)

print(results)
