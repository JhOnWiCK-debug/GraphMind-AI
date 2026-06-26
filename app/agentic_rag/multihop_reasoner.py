def multihop_query(
    graph,
    start_entity,
    first_relation,
    second_relation
):

    if start_entity not in graph:

        return None

    first_target = None

    for neighbor in graph.neighbors(
        start_entity
    ):

        relation = graph[
            start_entity
        ][
            neighbor
        ][
            "relation"
        ]

        if relation == first_relation:

            first_target = neighbor
            break

    if not first_target:

        return None

    for neighbor in graph.neighbors(
        first_target
    ):

        relation = graph[
            first_target
        ][
            neighbor
        ][
            "relation"
        ]

        if relation == second_relation:

            return neighbor

    return None