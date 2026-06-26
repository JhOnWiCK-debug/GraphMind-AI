from entity_extractor import (
    extract_question_entity
)

from relation_extractor import (
    extract_relation
)

from graph.graph_reasoner import answer_graph_question


def graph_qa(
    graph,
    question
):

    entity = extract_question_entity(
        graph,
        question
    )

    if not entity:

        return None

    relation = extract_relation(
        graph,
        entity,
        question
    )

    if not relation:

        return None

    answer = answer_graph_question(
        graph,
        entity,
        relation
    )

    return answer