from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3:8b"
)


def faiss_agent(
    question,
    retriever
):

    chunks = retriever.retrieve(
        question,
        k=3
    )

    print("\nRETRIEVED CHUNKS:\n")

    for i, chunk in enumerate(
        chunks
    ):

        print(
            f"\n--- Chunk {i+1} ---\n"
        )

        print(
            chunk[:500]
        )

    context = "\n\n".join(
        chunks
    )

    prompt = f"""
Answer the question using only
the provided context.

If the answer is not found,
say exactly:

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