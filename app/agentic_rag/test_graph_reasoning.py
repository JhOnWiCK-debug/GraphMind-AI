import pickle

from graph_query import (
    get_related_entities
)

with open(
    "knowledge_graph.pkl",
    "rb"
) as f:

    graph = pickle.load(
        f
    )

entity = input(
    "Entity: "
)

results = get_related_entities(
    graph,
    entity
)

print()

for relation, target in results:

    print(
        f"{relation} -> {target}"
    )