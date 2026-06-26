from planner_agent import (
    plan_query
)

while True:

    question = input(
        "\nQuestion: "
    )

    result = plan_query(
        question
    )

    print(
        "\nRoute:",
        result
    )