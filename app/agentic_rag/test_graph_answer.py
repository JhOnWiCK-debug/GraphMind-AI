import pickle

from graph_answer import (
    get_graph_answer
)

with open(
    "knowledge_graph.pkl",
    "rb"
) as f:

    graph = pickle.load(
        f
    )

answer = get_graph_answer(
    graph,
    "What currency does India use?"
)

print(
    answer
)