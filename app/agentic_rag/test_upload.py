# test_upload.py

import streamlit as st
from pdf_uploader import upload_pdf

st.title(
    "PDF Upload Test"
)

path = upload_pdf()

if path:

    st.write(
        f"Stored at: {path}"
    )