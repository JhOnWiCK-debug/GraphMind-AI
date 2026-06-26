import pickle

from dynamic_graph_answer import (
    get_dynamic_graph_answer
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

    answer = get_dynamic_graph_answer(
        graph,
        question
    )

    print(
        "Answer:",
        answer
    )