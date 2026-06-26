from pdf_processor import extract_text
from text_chunker import chunk_text

text = extract_text(
    "data/uploads/campus_assessment.pdf"
)

chunks = chunk_text(
    text
)

print(
    f"Chunks: {len(chunks)}"
)

print()

print(
    chunks[0]
)