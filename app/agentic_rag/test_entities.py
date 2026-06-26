from pdf_processor import extract_text
from entity_extractor import extract_entities

text = extract_text(
    "data/uploads/campus_assessment.pdf"
)

entities = extract_entities(
    text[:5000]
)

for entity in entities[:50]:

    print(entity)