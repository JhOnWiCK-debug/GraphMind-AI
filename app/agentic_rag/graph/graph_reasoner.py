from .graph_query import (
    get_related_entities
)


def answer_graph_question(
    graph,
    entity,
    relation
):

    results = get_related_entities(
        graph,
        entity
    )

    for rel, value in results:

        if rel == relation:

            return value

    return None