def extract_relation(
    graph,
    entity,
    question
):

    question = question.lower()

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

        relation_words = relation.replace(
            "_",
            " "
        )

        if (
            relation in question
            or relation_words in question
        ):

            return relation

    return None