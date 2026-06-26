from build_knowledge_graph import (
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
    )

]

graph = build_knowledge_graph(
    relationships
)

result = hybrid_reason(

    graph,

    "India",

    "currency",

    "India uses INR as its currency."

)

print(
    result
)