from graph_query import (
    get_related_entities
)


def graph_context(
    graph,
    entity
):

    facts = []

    results = get_related_entities(
        graph,
        entity
    )

    for relation, value in results:

        facts.append(
            f"{entity} {relation} {value}"
        )

    return "\n".join(
        facts
    )