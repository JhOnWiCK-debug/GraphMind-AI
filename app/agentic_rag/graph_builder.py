import networkx as nx


def build_graph(chunks):

    graph = nx.Graph()

    for i, chunk in enumerate(chunks):

        graph.add_node(
            i,
            text=chunk
        )

    for i in range(len(chunks) - 1):

        graph.add_edge(
            i,
            i + 1
        )

    return graph