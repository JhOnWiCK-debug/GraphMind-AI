import pickle

from question_understanding import (
    understand_question
)

with open(
    "knowledge_graph.pkl",
    "rb"
) as f:

    graph = pickle.load(
        f
    )

question = input(
    "Question: "
)

result = understand_question(
    question,
    graph
)

print(
    "\nResult:",
    result
)