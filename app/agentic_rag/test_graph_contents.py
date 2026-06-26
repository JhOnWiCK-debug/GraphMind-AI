import pickle

with open(
    "knowledge_graph.pkl",
    "rb"
) as f:

    graph = pickle.load(
        f
    )

print("\nNODES:\n")

for node in graph.nodes:
    print(node)

print("\nEDGES:\n")

for u, v, data in graph.edges(
    data=True
):
    print(
        f"{u} --{data['relation']}--> {v}"
    )