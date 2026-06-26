from graph_reasoner import (
    answer_graph_question
)


def hybrid_reason(
    graph,
    entity,
    relation,
    context
):

    graph_answer = answer_graph_question(
        graph,
        entity,
        relation
    )

    return {

        "graph_answer":
        graph_answer,

        "context":
        context

    }