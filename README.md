# 📚 AI PDF Navigator (RAG System)

A premium, modern PDF Retrieval-Augmented Generation (RAG) system built with **FastAPI**, **Next.js**, and **LangChain**. This application allows users to upload PDF documents and interact with them through an AI-powered chat interface.

---

## ✨ Features

- **Premium UI**: Sleek "Glassmorphism" design with smooth micro-animations.
- **Local Embeddings**: Uses `BAAI/bge-small-en-v1.5` for high-quality local text vectorization.
- **Groq Acceleration**: Powered by Llama 3.3 for lightning-fast responses.
- **Intelligent RAG**: Efficient document parsing (PyPDF) and vector search (FAISS).

---

## 🛠️ Tech Stack

- **Frontend**: Next.js, React, Vanilla CSS.
- **Backend**: FastAPI, Python.
- **AI Core**: LangChain, LangChain-Groq, LangChain-HuggingFace.
- **Vector DB**: FAISS.

---

## 🚀 Getting Started

### 1. Prerequisites
- **Python 3.10+**
- **Node.js 18+**
- **Groq API Key**: Get one at [console.groq.com](https://console.groq.com).

### 2. Backend Setup
1. Open a terminal in the `backend/` folder.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the `backend/` folder:
   ```env
   GROQ_API_KEY=your_key_here
   ```

### 3. Frontend Setup
1. Open a terminal in the `frontend/` folder.
2. Install packages:
   ```bash
   npm install
   ```

### 4. Running the Project
- **One-Click Start**: Double-click `run.bat` in the root directory.
- **Manual Start**:
  - Backend: `uvicorn main:app --reload` (inside `backend/` with venv active)
  - Frontend: `npm run dev` (inside `frontend/`)

---

## 🔧 Troubleshooting

- **ModuleNotFoundError (LangChain)**: If you experience issues with missing LangChain modules, ensure you are using the official framework (v0.3.x) by running:
  ```bash
  pip install langchain langchain-community langchain-huggingface langchain-groq --force-reinstall
  ```
- **Virtual Memory Issues**: Large models may require more page file size. Close background apps if the server fails to load the embedding model.

---

## 📜 License

Created as part of a custom PDF RAG project.
