from knowledge_graph_builder import (
    build_knowledge_graph
)

from graph_reasoner import (
    answer_graph_question
)

graph = build_knowledge_graph()

answer = answer_graph_question(
    graph,
    "India",
    "currency"
)

print(
    answer
)