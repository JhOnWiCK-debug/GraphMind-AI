def get_related_entities(
    graph,
    entity
):

    results = []

    if entity not in graph:

        return results

    for neighbor in graph.neighbors(
        entity
    ):

        relation = graph[
            entity
        ][
            neighbor
        ][
            "relation"
        ]

        results.append(
            (
                relation,
                neighbor
            )
        )

    return results