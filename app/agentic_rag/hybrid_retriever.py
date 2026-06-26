from graph.graph_retriever


def hybrid_retrieve(
    graph,
    vector_results
):

    retrieved_nodes = []

    for idx in vector_results:

        nodes = graph_search(
            graph,
            idx,
            depth=1
        )

        retrieved_nodes.extend(
            nodes
        )

    return list(
        set(retrieved_nodes)
    )