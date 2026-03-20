# Developer Notes: PDF RAG Architecture

This document outlines the technical design and architectural choices for the AI PDF Navigator.

---

## 🏗️ Architecture Overview
The system follows a classic **Retrieval-Augmented Generation (RAG)** pattern:

1.  **Ingestion Layer**: `PyPDFLoader` extracts text, and `RecursiveCharacterTextSplitter` chunks it (1000 chars with 100 char overlap).
2.  **Embedding Layer**: Uses `BAAI/bge-small-en-v1.5` via `langchain-huggingface`. Runs **locally on CPU**.
3.  **Vector Store**: `FAISS` handles local vector search.
4.  **Inference Layer**: `ChatGroq` (Llama 3.3-70b-versatile) via Groq's LPU technology.

---

## 🔄 Execution Flow

### Backend (Python/FastAPI)
- **`main.py`**: Entry point. Manages `/upload` (PDF storage & indexing) and `/ask` (query handling) endpoints.
- **`rag_logic.py`**: The "Brain".
    - **Chunking**: Breaks text into pieces to maintain semantic relevance.
    - **Vectorization**: Transforms text into numerical data for similarity matching.
    - **Retrieval**: Finds the top relevant chunks for any given question.
    - **LLM Orchestration**: Combines retrieved context with the user query for Groq.

### Frontend (Next.js/React)
- **`app/page.tsx`**: The "Interface".
    - **State Management**: Reactive UI updates for messages and loading states.
    - **API Integration**: Asynchronous `fetch` calls to backend endpoints.
- **`app/globals.css`**: The "Aesthetics".
    - Implements a high-end **Glassmorphism** design system with a dark-mode first approach.

---

## 🛠️ Tech Stack Decisions
- **FastAPI**: Performance and automatic Swagger documentation.
- **Next.js 14+**: Modern App Router and server-side optimization.
- **Vanilla CSS**: Used for bespoke, premium visuals over standard utility frameworks.

---

## 🚀 Future Roadmap
- [ ] **Persistent Vector Store**: Migration to Qdrant or ChromaDB.
- [ ] **Streaming Responses**: Real-time token streaming with SSE.
- [ ] **User Persistence**: SQLite integration for session history.
