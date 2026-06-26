from graph.build_knowledge_graph import (
    build_knowledge_graph
)

from graph.graph_reasoner import answer_graph_question

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

answer = answer_graph_question(
    graph,
    "India",
    "currency"
)

print(
    answer
)