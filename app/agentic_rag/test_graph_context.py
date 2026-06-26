from knowledge_graph_builder import (
    build_knowledge_graph
)

from graph_context import (
    graph_context
)

graph = build_knowledge_graph()

entity = input(
    "Entity: "
)

context = graph_context(
    graph,
    entity
)

print(
    "\nGraph Context:\n"
)

print(
    context
)