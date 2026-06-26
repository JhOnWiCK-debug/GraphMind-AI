from pdf_processor import extract_text
from llm_entity_extractor import extract_entities

text = extract_text(
    "data/uploads/campus_assessment.pdf"
)

entities = extract_entities(
    text
)

print(
    entities
)