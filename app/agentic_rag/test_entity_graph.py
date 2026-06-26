from pdf_processor import extract_text

from llm_entity_extractor import (
    extract_entities
)

from entity_graph_builder import (
    build_entity_graph
)

text = extract_text(
    "data/uploads/campus_assessment.pdf"
)

entities_text = extract_entities(
    text
)

entities = eval(
    entities_text.split(":")[-1].strip()
)

graph = build_entity_graph(
    entities
)

print(
    "Nodes:",
    graph.number_of_nodes()
)

print(
    "Edges:",
    graph.number_of_edges()
)

print()

for edge in graph.edges():

    print(edge)