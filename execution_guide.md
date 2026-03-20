# Full Manual: AI PDF Navigator

This guide provides everything you need to know to set up, run, and troubleshoot the PDF RAG system.

---

## 📋 Prerequisites

Before starting, ensure you have the following installed on your Windows machine:
1.  **Python 3.10 or higher**: [Download here](https://www.python.org/downloads/)
2.  **Node.js 18 or higher**: [Download here](https://nodejs.org/)
3.  **Groq API Key**: Create a free account and get your key at [console.groq.com](https://console.groq.com).

---

## 🛠️ Installation & Setup

### 1. Backend Setup
The backend handles PDF processing and the AI "brain".
1.  Open a terminal in the `backend/` folder.
2.  Create a virtual environment:
    ```powershell
    python -m venv venv
    ```
3.  Activate the environment:
    ```powershell
    .\venv\Scripts\activate
    ```
4.  Install dependencies:
    ```powershell
    pip install -r requirements.txt
    ```
5.  **Configure API Key**: In the `backend/` folder, ensure your key is in the `.env` file:
    ```env
    GROQ_API_KEY=gsk_your_key_here
    ```

### 2. Frontend Setup
The frontend is the premium "glassmorphism" user interface.
1.  Open a terminal in the `frontend/` folder.
2.  Install packages:
    ```powershell
    npm install
    ```

---

## 🚀 Running the Project

### Option A: The "One-Click" Method (Recommended)
Simply double-click the **`run.bat`** file in the project's root directory. It will automatically:
- Start the FastAPI backend in one window.
- Start the Next.js frontend in a second window.

### Option B: Manual Execution
If you prefer to run them separately:
- **Backend**: `cd backend; .\venv\Scripts\activate; uvicorn main:app --reload`
- **Frontend**: `cd frontend; npm run dev`

---

## 📖 How to Use the RAG System

1.  **Launch the UI**: Go to [http://localhost:3000](http://localhost:3000) in your browser.
2.  **Upload a PDF**:
    - Click the dashed upload area.
    - Select a PDF (use the included `sample.pdf` in the `backend/` folder for testing).
    - Wait for the "PDF processed successfully" status.
3.  **Ask a Question**:
    - Type a question about the PDF in the bottom input box (e.g., "Summarize this document").
    - Press **Enter** or click **Ask**.
    - Watch the AI navigate your document and provide an instant answer.

---

## 🔧 Troubleshooting

### "Invalid API Key" Error
- Ensure you have pasted your key correctly in `backend/.env`.
- **Important**: You MUST restart the backend server after changing the API key.

### "Paging file too small" (OS Error 1455)
- This happens if Windows runs out of virtual memory while loading the embedding model.
- **Fix**: Close other heavy apps (like Chrome, Discord, or Minecraft) or increase your Windows Page File size in System Settings.

### Frontend won't start
- Ensure you have run `npm install` in the `frontend/` folder first.
- Check if another app is already using port 3000.
