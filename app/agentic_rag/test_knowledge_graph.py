from knowledge_graph_builder import (
    build_knowledge_graph
)

graph = build_knowledge_graph()

for u, v, data in graph.edges(
    data=True
):

    print(
        u,
        data["relation"],
        v
    )