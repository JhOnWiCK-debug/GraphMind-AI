import networkx as nx


def graph_search(
    graph,
    start_node,
    depth=1
):

    visited = set()

    queue = [
        start_node
    ]

    for _ in range(depth):

        next_queue = []

        for node in queue:

            neighbors = list(
                graph.neighbors(node)
            )

            next_queue.extend(
                neighbors
            )

            visited.add(node)

        queue = next_queue

    visited.update(queue)

    return list(visited)