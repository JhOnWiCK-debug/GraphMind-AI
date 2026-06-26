from agent_router import (
    route_query
)

while True:

    question = input(
        "\nQuestion: "
    )

    route, agent = route_query(
        question
    )

    print(
        "\nRoute:",
        route
    )

    print(
        "Agent:",
        agent
    )