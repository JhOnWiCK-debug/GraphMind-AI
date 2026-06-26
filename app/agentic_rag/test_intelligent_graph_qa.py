import pickle

from graph.intelligent_graph_qa import (
    intelligent_graph_qa
)

with open(
    "knowledge_graph.pkl",
    "rb"
) as f:

    graph = pickle.load(
        f
    )

while True:

    question = input(
        "\nQuestion: "
    )

    answer = intelligent_graph_qa(
        graph,
        question
    )

    print(
        "Answer:",
        answer
    )