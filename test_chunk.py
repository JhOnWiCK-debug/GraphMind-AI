from app.pdf_processing.process_pdf import read_pdf
from app.pdf_processing.chunker import chunk_text

text = read_pdf(
    "data/Vishva_M_Resume_OnePage_pdf.pdf"
)

chunks = chunk_text(text)

print(
    "Chunks:",
    len(chunks)
)

print(
    chunks[0]
)