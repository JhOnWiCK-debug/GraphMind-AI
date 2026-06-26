import pickle

from entity_extractor import (
    extract_question_entity
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

entity = extract_question_entity(
    graph,
    question
)

print(
    "\nEntity:",
    entity
)