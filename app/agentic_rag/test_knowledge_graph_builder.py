from knowledge_graph_builder import (
    build_knowledge_graph_from_relationships
)

relationships = [

    (
        "India",
        "currency",
        "INR"
    ),

    (
        "Wheelz",
        "imports_from",
        "China"
    )

]

graph = build_knowledge_graph_from_relationships(
    relationships
)

for u, v, data in graph.edges(
    data=True
):

    print(
        f"{u} --{data['relation']}--> {v}"
    )