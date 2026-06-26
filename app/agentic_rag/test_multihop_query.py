import networkx as nx

from multihop_reasoner import (
    multihop_query
)

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

answer = multihop_query(
    graph,
    "Wheelz",
    "imports_from",
    "currency"
)

print(
    "\nAnswer:",
    answer
)