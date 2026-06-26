import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from pdf_processing.process_pdf import read_pdf
from pdf_processing.chunker import chunk_text
from pdf_processing.embed_and_store import store_chunks

import streamlit as st
import chromadb

from sentence_transformers import SentenceTransformer
from langchain_ollama import ChatOllama


# -----------------------
# PAGE
# -----------------------

st.set_page_config(
    page_title="Agentic RAG",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Agentic RAG Chatbot")


# -----------------------
# SIDEBAR
# -----------------------

with st.sidebar:

    st.title("🚀 Agentic RAG")

    st.write("Powered by:")
    st.write("• ChromaDB")
    st.write("• Llama 3")
    st.write("• Ollama")
    st.write("• LangChain")

    st.divider()


# -----------------------
# PDF UPLOAD
# -----------------------

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs(
        "data/uploads",
        exist_ok=True
    )

    file_path = os.path.join(
        "data/uploads",
        uploaded_file.name
    )

    with open(
        file_path,
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    text = read_pdf(
        file_path
    )

    chunks = chunk_text(
        text
    )

    count = store_chunks(
        chunks
    )

    st.success(
        f"Stored {count} chunks from {uploaded_file.name}"
    )


# -----------------------
# MODELS
# -----------------------

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

llm = ChatOllama(
    model="llama3:8b"
)

client = chromadb.PersistentClient(
    path="./vector_store"
)

collection = client.get_collection(
    "documents"
)


# -----------------------
# CHAT HISTORY
# -----------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"]
    ):
        st.write(
            msg["content"]
        )


# -----------------------
# CHAT INPUT
# -----------------------

question = st.chat_input(
    "Ask a question"
)

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    query_embedding = embedding_model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n".join(
        results["documents"][0]
    )

    prompt = f"""
You are a document assistant.

Rules:
1. Answer only using the provided context.
2. If the answer is not found in the context, say:
   "I could not find that information in the uploaded document."
3. Do not use outside knowledge.
4. Be concise and accurate.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(
        prompt
    )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.content
        }
    )

    st.rerun()