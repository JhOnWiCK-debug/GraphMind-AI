import pickle

from graph_qa import (
    graph_qa
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

    answer = graph_qa(
        graph,
        question
    )

    print(
        "Answer:",
        answer
    )