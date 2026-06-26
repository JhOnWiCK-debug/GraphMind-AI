import networkx as nx


def build_knowledge_graph(
    relationships
):

    graph = nx.DiGraph()

    for source, relation, target in relationships:

        if (
            source is None
            or relation is None
            or target is None
        ):
            continue

        if (
            str(source).strip() == ""
            or str(relation).strip() == ""
            or str(target).strip() == ""
        ):
            continue

        graph.add_edge(
            str(source).strip(),
            str(target).strip(),
            relation=str(relation).strip()
        )

    return graph