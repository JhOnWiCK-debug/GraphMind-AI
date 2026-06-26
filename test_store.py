from app.pdf_processing.process_pdf import read_pdf
from app.pdf_processing.chunker import chunk_text
from app.pdf_processing.embed_and_store import store_chunks

text = read_pdf(
    "data/Vishva_M_Resume_OnePage_pdf.pdf"
)

chunks = chunk_text(text)

count = store_chunks(chunks)

print(
    f"Stored {count} chunks"
)