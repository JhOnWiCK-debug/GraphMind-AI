from knowledge_graph_builder import (
    build_knowledge_graph
)

from graph_query import (
    get_related_entities
)

graph = build_knowledge_graph()

results = get_related_entities(
    graph,
    "India"
)

print(
    results
)