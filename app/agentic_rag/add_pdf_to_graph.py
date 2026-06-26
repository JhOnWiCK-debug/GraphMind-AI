import pickle
import networkx as nx

from pdf_processor import extract_text
from text_chunker import chunk_text


def add_pdf_to_graph(pdf_path):

    text = extract_text(
        pdf_path
    )

    chunks = chunk_text(
        text
    )

    with open(
        "graph.pkl",
        "rb"
    ) as f:

        graph = pickle.load(
            f
        )

    with open(
        "chunk_mapping.pkl",
        "rb"
    ) as f:

        chunk_mapping = pickle.load(
            f
        )

    start_node = len(
        graph.nodes
    )

    for i, chunk in enumerate(
        chunks
    ):

        node_id = start_node + i

        graph.add_node(
            node_id,
            text=chunk
        )

        chunk_mapping[
            chunk
        ] = node_id

        if i > 0:

            graph.add_edge(
                node_id - 1,
                node_id
            )

    with open(
        "graph.pkl",
        "wb"
    ) as f:

        pickle.dump(
            graph,
            f
        )

    with open(
        "chunk_mapping.pkl",
        "wb"
    ) as f:

        pickle.dump(
            chunk_mapping,
            f
        )

    print(
        f"Added {len(chunks)} graph nodes"
    )