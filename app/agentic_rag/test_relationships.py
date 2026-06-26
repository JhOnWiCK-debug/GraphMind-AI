from pdf_processor import extract_text
from relationship_extractor import extract_relationships

text = extract_text(
    "data/uploads/campus_assessment.pdf"
)

relationships = extract_relationships(
    text
)

print(
    relationships
)