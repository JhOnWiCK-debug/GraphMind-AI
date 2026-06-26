from app.pdf_processing.process_pdf import read_pdf

text = read_pdf(
    "data/Vishva_M_Resume_OnePage_pdf.pdf"
)

print(text[:1000])