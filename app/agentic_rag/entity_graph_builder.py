import networkx as nx


def build_entity_graph(
    entities
):

    graph = nx.Graph()

    for entity in entities:

        graph.add_node(
            entity
        )

    for i in range(
        len(entities) - 1
    ):

        graph.add_edge(
            entities[i],
            entities[i + 1]
        )

    return graph