from planner_agent import (
    plan_query
)


def route_query(
    question
):

    route = plan_query(
        question
    )

    if route == "GRAPH":

        return (
            route,
            "GRAPH_AGENT"
        )

    elif route == "FAISS":

        return (
            route,
            "RETRIEVER_AGENT"
        )

    elif route == "HYBRID":

        return (
            route,
            "HYBRID_AGENT"
        )

    elif route == "SUMMARY":

        return (
            route,
            "SUMMARY_AGENT"
    )    

    return (
        "UNKNOWN",
        None
    )