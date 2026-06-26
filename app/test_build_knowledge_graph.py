from build_knowledge_graph import (
    build_knowledge_graph
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

graph = build_knowledge_graph(
    relationships
)

for u, v, data in graph.edges(
    data=True
):

    print(
        f"{u} --{data['relation']}--> {v}"
    )