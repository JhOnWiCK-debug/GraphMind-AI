from graph.graph_reasoner import answer_graph_question


def get_dynamic_graph_answer(
    graph,
    question
):

    question = question.lower()

    for node in graph.nodes:

        if str(node).lower() in question:

            for neighbor in graph.neighbors(
                node
            ):

                relation = graph[
                    node
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

                    return neighbor

    return None