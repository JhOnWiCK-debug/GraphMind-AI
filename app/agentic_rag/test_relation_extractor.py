import pickle

from entity_extractor import (
    extract_question_entity
)

from relation_extractor import (
    extract_relation
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

relation = extract_relation(
    graph,
    entity,
    question
)

print(
    "\nEntity:",
    entity
)

print(
    "Relation:",
    relation
)