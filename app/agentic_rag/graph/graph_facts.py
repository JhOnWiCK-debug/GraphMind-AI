def get_graph_facts(
    graph
):

    facts = []

    for source, target, data in graph.edges(
        data=True
    ):

        relation = data[
            "relation"
        ]

        facts.append(
            f"{source} {relation} {target}"
        )

    return "\n".join(
        facts
    )