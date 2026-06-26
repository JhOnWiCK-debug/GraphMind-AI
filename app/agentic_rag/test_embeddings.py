from pdf_processor import extract_text
from text_chunker import chunk_text
from retrieval.embed_chunks import embed_chunks

text = extract_text(
    "data/uploads/campus_assessment.pdf"
)

chunks = chunk_text(
    text
)

embeddings = embed_chunks(
    chunks
)

print(
    f"Chunks: {len(chunks)}"
)

print(
    f"Embeddings: {len(embeddings)}"
)

print(
    f"Dimension: {len(embeddings[0])}"
)