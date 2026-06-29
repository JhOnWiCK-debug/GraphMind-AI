from .graph_reasoner import answer_graph_question


def get_graph_answer(
    graph,
    question
):

    question = question.lower()

    if (
        "currency" in question
        and "india" in question
    ):

        answer = answer_graph_question(
            graph,
            "India",
            "currency"
        )

        return answer

    return None