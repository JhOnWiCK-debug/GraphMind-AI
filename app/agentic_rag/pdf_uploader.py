import os
import streamlit as st

from document_pipeline import (
    process_document
)

UPLOAD_FOLDER = "data/uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)


def upload_pdf():

    uploaded_file = st.file_uploader(
        "Upload a PDF",
        type=["pdf"]
    )

    if uploaded_file:

        save_path = os.path.join(
            UPLOAD_FOLDER,
            uploaded_file.name
        )

        with open(
            save_path,
            "wb"
        ) as f:

            f.write(
                uploaded_file.getbuffer()
            )

        st.success(
            f"Saved: {uploaded_file.name}"
        )

        with st.spinner(
            "Building GraphRAG Knowledge Base..."
        ):

            process_document(
                save_path
            )

        st.success(
            "GraphRAG Pipeline Complete"
        )

        return save_path

    return None