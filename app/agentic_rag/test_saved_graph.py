import pickle

with open(
    "knowledge_graph.pkl",
    "rb"
) as f:

    graph = pickle.load(
        f
    )

print(
    f"Nodes: {graph.number_of_nodes()}"
)

print(
    f"Edges: {graph.number_of_edges()}"
)

print()

for u, v, data in graph.edges(
    data=True
):

    print(
        f"{u} --{data['relation']}--> {v}"
    )