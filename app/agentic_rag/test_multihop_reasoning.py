import networkx as nx

graph = nx.DiGraph()

graph.add_edge(
    "Wheelz",
    "China",
    relation="imports_from"
)

graph.add_edge(
    "China",
    "Yuan",
    relation="currency"
)

print("\nEDGES:\n")

for u, v, data in graph.edges(
    data=True
):

    print(
        f"{u} --{data['relation']}--> {v}"
    )