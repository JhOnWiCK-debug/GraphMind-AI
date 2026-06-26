import streamlit as st
import pickle

from retrieval.faiss_store import FAISSStore
from retrieval.faiss_retriever import FAISSRetriever
from graph.graph_retriever

from langchain_ollama import ChatOllama
from pdf_uploader import upload_pdf
from critic import evaluate_answer
from graph.intelligent_graph_qa import (
    intelligent_graph_qa
)


# -------------------
# LOAD EVERYTHING
# -------------------

store = FAISSStore.load(
    "faiss.index",
    "documents.pkl"
)

retriever = FAISSRetriever(
    store
)

with open(
    "graph.pkl",
    "rb"
) as f:

    graph = pickle.load(
        f
    )

with open(
    "chunk_mapping.pkl",
    "rb"
) as f:

    chunk_mapping = pickle.load(
        f
    )

with open(
    "knowledge_graph.pkl",
    "rb"
) as f:

    knowledge_graph = pickle.load(
        f
    )

llm = ChatOllama(
    model="llama3:8b"
)


# -------------------
# RETRIEVAL
# -------------------

def retrieve_context(question):

    results = retriever.retrieve(
        question,
        k=3
    )

    expanded_chunks = []

    for chunk in results:

        expanded_chunks.append(
            chunk
        )

        if chunk in chunk_mapping:

            node_id = chunk_mapping[
                chunk
            ]

            neighbors = graph_search(
                graph,
                node_id,
                depth=1
            )

            for neighbor in neighbors:

                expanded_chunks.append(
                    graph.nodes[
                        neighbor
                    ]["text"]
                )

    expanded_chunks = list(
        dict.fromkeys(
            expanded_chunks
        )
    )

    return (
        "\n".join(
            expanded_chunks
        ),
        expanded_chunks
    )


# -------------------
# ANSWER
# -------------------

def generate_answer(
    question,
    context
):

    prompt = f"""
You are a document assistant.

Answer naturally.

Rules:
- Use only information from the context.
- Do not mention "according to the context".
- Answer directly.
- If not found, say exactly:
I could not find that information in the uploaded documents.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(
        prompt
    )

    return response.content


# -------------------
# UI
# -------------------

st.set_page_config(
    page_title="GraphRAG",
    page_icon="🤖",
    layout="wide"
)

st.title(
    "🤖 Agentic GraphRAG"
)
uploaded_pdf = upload_pdf()

# -------------------
# SIDEBAR
# -------------------

st.sidebar.title(
    "📊 System Metrics"
)

st.sidebar.metric(
    "Graph Nodes",
    len(graph.nodes)
)

st.sidebar.metric(
    "Documents Indexed",
    len(store.documents)
)

# -------------------
# CHAT HISTORY
# -------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(
        message["role"]
    ):

        st.write(
            message["content"]
        )

# -------------------
# INPUT
# -------------------
question = st.chat_input(
    "Ask something about your documents..."
)

if question:

    # show user message
    with st.chat_message(
        "user"
    ):
        st.write(
            question
        )

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    # retrieve context
    context, sources = retrieve_context(
        question
    )

    # graph-first reasoning
    graph_answer = intelligent_graph_qa(
    knowledge_graph,
    question
   )

    print("\nQUESTION:")
    print(question)

    print("\nGRAPH ANSWER:")
    print(graph_answer)

    if graph_answer:

        answer = graph_answer
        verdict = "GRAPH ANSWER"

    else:

        answer = generate_answer(
            question,
            context
        )

        verdict = evaluate_answer(
            question,
            context,
            answer
        )

    # metrics
    retrieved_chunks = len(
        sources
    )

    context_length = len(
        context
    )

    # save answer
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    # display answer
    with st.chat_message(
        "assistant"
    ):

        st.write(
            answer
        )

    # verdict
    if verdict == "GRAPH ANSWER":

        st.success(
            "🧠 Answered from Knowledge Graph"
        )

    elif "YES" in verdict.upper():

        st.success(
            "✅ Answer Supported by Context"
        )

    else:

        st.error(
            "❌ Answer Not Fully Supported"
        )

    # retrieval metrics
    with st.expander(
        "📈 Retrieval Metrics"
    ):

        st.write(
            f"Retrieved Chunks: {retrieved_chunks}"
        )

        st.write(
            f"Context Length: {context_length}"
        )

        st.write(
            f"Critic Verdict: {verdict}"
        )

    # sources
    with st.expander(
        "📄 Sources Used"
    ):

        for i, source in enumerate(
            sources[:5]
        ):

            st.markdown(
                f"### Source {i+1}"
            )

            st.write(
                source[:500]
            )

            st.divider()

    # raw context
    with st.expander(
        "🔍 Retrieved Context"
    ):

        st.text_area(
            "Context",
            context,
            height=300
        )

    st.rerun()