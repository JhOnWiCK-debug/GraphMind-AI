from .agent_router import (
    route_query
)

from .graph.intelligent_graph_qa import (
    intelligent_graph_qa
)

from .faiss_agent import (
    faiss_agent
)

from .document_summary_agent import (
    summarize_document
)

from .hybrid_agent import (
    hybrid_agent
)


def run_agent(
    question,
    knowledge_graph,
    retriever,
    documents
):

    route, agent = route_query(
        question
    )

    print(
        f"\nRoute: {route}"
    )

    print(
        f"Agent: {agent}"
    )

    # GRAPH AGENT

    if route == "GRAPH":

        return intelligent_graph_qa(
            knowledge_graph,
            question
        )

    # FAISS AGENT

    elif route == "FAISS":

        return faiss_agent(
            question,
            retriever
        )

    # SUMMARY AGENT

    elif route == "SUMMARY":

        return summarize_document(
            documents
        )

    # HYBRID AGENT

    elif route == "HYBRID":

        return hybrid_agent(
            question,
            knowledge_graph,
            retriever
        )

    return "No suitable agent found."