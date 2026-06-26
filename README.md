# 🚀 GraphMind AI

> **Enterprise Agentic GraphRAG Platform**
> Hybrid Retrieval • Knowledge Graph Reasoning • Multi-Hop QA • Persistent Memory • Local LLMs

![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

GraphMind AI is an enterprise-style **Agentic GraphRAG platform** that combines semantic retrieval, knowledge graphs, and intelligent routing to answer complex questions from documents.

Unlike traditional RAG systems that only retrieve document chunks, GraphMind AI can:

* Search vector databases
* Traverse knowledge graphs
* Perform multi-hop reasoning
* Maintain conversation memory
* Select the best reasoning strategy automatically

The goal is to build a production-ready AI platform capable of enterprise document intelligence.

---

# ✨ Current Features

### 📄 Document Intelligence

* PDF ingestion
* Intelligent chunking
* Sentence Transformer embeddings
* FAISS vector search

### 🧠 Knowledge Graph

* Entity extraction
* Relationship extraction
* Knowledge graph construction
* Graph querying

### 🤖 Multi-Agent Architecture

* Planner Agent
* Router Agent
* Graph Agent
* FAISS Retrieval Agent
* Summary Agent
* Hybrid Agent

### 🔍 Advanced Reasoning

* Multi-hop graph traversal
* Hybrid Graph + Vector retrieval
* Source attribution
* Conversation memory
* Persistent memory

---

# 🏗 System Architecture

```text
                    User Question
                          │
                          ▼
                  Planner Agent
                          │
                          ▼
                   Router Agent
      ┌──────────────┼──────────────┐
      ▼              ▼              ▼
 Graph Agent    FAISS Agent   Summary Agent
      │              │              │
      └──────────────┼──────────────┘
                     ▼
               Hybrid Agent
                     ▼
            Final AI Response
```

---

# 🧠 Example Queries

### Graph Reasoning

```
Where does Wheelz import from?
```

Answer

```
China
```

---

### Multi-Hop Reasoning

```
What currency is used in the country Wheelz imports from?
```

Answer

```
Yuan
```

---

### Document Understanding

```
Summarize the uploaded document.
```

---

# 🛠 Tech Stack

| Category        | Technologies                |
| --------------- | --------------------------- |
| Language        | Python                      |
| LLM             | Ollama (Llama 3)            |
| Vector Search   | FAISS                       |
| Knowledge Graph | NetworkX                    |
| Embeddings      | Sentence Transformers       |
| NLP             | spaCy                       |
| Framework       | LangChain                   |
| Agent Workflow  | Custom Agentic Architecture |

---

# 📂 Project Structure

```text
app/
└── agentic_rag/
    ├── agents/
    ├── config/
    ├── evaluation/
    ├── graph/
    ├── ingestion/
    ├── memory/
    ├── retrieval/
    ├── tests/
    └── utils/
```

---

# 🚀 Roadmap

## Completed

* Knowledge Graph
* Graph QA
* Multi-Hop Reasoning
* Hybrid Retrieval
* Planner Agent
* Router Agent
* Summary Agent
* Persistent Memory
* Source Attribution
* Modular Architecture

## In Progress

* FastAPI Backend
* REST API
* Swagger Documentation

## Planned

* Docker Deployment
* Authentication
* PostgreSQL
* Interactive Graph Visualization
* Cross-Encoder Reranking
* Web Dashboard
* Cloud Deployment

---

# 📊 Project Status

This project is under active development and is evolving into a production-grade Agentic GraphRAG platform.

---

# 👨‍💻 Author

**Vishva M**

AI • Machine Learning • Data Science

GitHub: https://github.com/JhOnWiCK-debug
