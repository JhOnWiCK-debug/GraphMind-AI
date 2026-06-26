from question_understanding import (
    understand_question
)

from graph_reasoner import (
    answer_graph_question
)


def intelligent_graph_qa(
    graph,
    question
):

    result = understand_question(
        question,
        graph
    )

    print("\nLLM OUTPUT:")
    print(result)

    lines = result.splitlines()

    for line in lines:

        if "|" in line:

            result = line.strip()
            break

    else:

        return None

    entity, relation = result.split(
        "|",
        1
    )

    answer = answer_graph_question(
        graph,
        entity.strip(),
        relation.strip()
    )

    return answer