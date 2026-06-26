from graph.build_knowledge_graph import (
    build_knowledge_graph
)

from hybrid_reasoner import (
    hybrid_reason
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

context = """
India uses INR as its currency.
Wheelz imports spare parts from China.
"""

result = hybrid_reason(

    graph,

    "India",

    "currency",

    context

)

print("\nGraph Answer:")
print(result["graph_answer"])

print("\nContext:")
print(result["context"])