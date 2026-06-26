from typing import TypedDict

import chromadb
from sentence_transformers import SentenceTransformer
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, END

from critic import evaluate_answer
from query_rewriter import rewrite_query


# -------------------
# STATE
# -------------------

class GraphState(TypedDict):
    question: str
    context: str
    answer: str
    reflection: str
    attempts: int


# -------------------
# MODELS
# -------------------

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


# -------------------
# NODES
# -------------------

def planner(state):

    print("\nPlanner Running")

    return state


def retriever(state):

    print("Retriever Running")
    
    state["attempts"] += 1
    query_embedding = embedding_model.encode(
        state["question"]
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    context = "\n".join(
        results["documents"][0]
    )

    state["context"] = context

    return state


def reasoner(state):

    print("Reasoner Running")

    prompt = f"""
Answer only from the context.

Context:
{state['context']}

Question:
{state['question']}
"""

    response = llm.invoke(prompt)

    state["answer"] = response.content

    return state


def reflection(state):

    print("Critic Running")

    verdict = evaluate_answer(
        state["question"],
        state["context"],
        state["answer"]
    )

    state["reflection"] = verdict

    return state

def rewrite(state):

    print("Query Rewriter Running")

    new_question = rewrite_query(
        state["question"]
    )

    print(
        f"Rewritten Query: {new_question}"
    )

    state["question"] = new_question

    return state

def route_after_reflection(state):

    print(
        f"Critic Verdict: {state['reflection']}"
    )

    if "YES" in state["reflection"].upper():
        return END

    if state["attempts"] >= 3:
        return END

    return "rewrite"
# -------------------
# GRAPH
# -------------------

workflow = StateGraph(GraphState)

workflow.add_node(
    "planner",
    planner
)

workflow.add_node(
    "retriever",
    retriever
)

workflow.add_node(
    "reasoner",
    reasoner
)

workflow.add_node(
    "reflection",
    reflection
)
workflow.add_node(
    "rewrite",
    rewrite
)

workflow.set_entry_point(
    "planner"
)

workflow.add_edge(
    "planner",
    "retriever"
)

workflow.add_edge(
    "retriever",
    "reasoner"
)

workflow.add_edge(
    "reasoner",
    "reflection"
)

workflow.add_conditional_edges(
    "reflection",
    route_after_reflection,
    {
        "rewrite": "rewrite",
        END: END
    }
)
workflow.add_edge(
    "rewrite",
    "retriever"
)

graph = workflow.compile()


# -------------------
# RUN
# -------------------

question = input(
    "\nAsk a Question: "
)

result = graph.invoke(
    {
        "question": question,
        "context": "",
        "answer": "",
        "reflection": "",
        "attempts": 0
    }
)

print("\nFINAL ANSWER:\n")

print(result["answer"])

print("\nREFLECTION:")

print(result["reflection"])