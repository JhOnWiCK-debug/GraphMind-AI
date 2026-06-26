import os

from pypdf import PdfReader


def load_documents(folder_path):

    all_text = []

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            pdf_path = os.path.join(
                folder_path,
                file
            )

            reader = PdfReader(
                pdf_path
            )

            text = ""

            for page in reader.pages:

                page_text = page.extract_text()

                if page_text:

                    text += page_text

            all_text.append(
                {
                    "filename": file,
                    "text": text
                }
            )

    return all_text