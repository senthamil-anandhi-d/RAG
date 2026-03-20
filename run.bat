@echo off
echo Starting PDF RAG System...

:: Start Backend
start cmd /k "cd backend && venv\Scripts\activate && uvicorn main:app --host 0.0.0.0 --port 8000"

:: Start Frontend
start cmd /k "cd frontend && npm run dev"

echo.
echo Backend will be at http://localhost:8000
echo Frontend will be at http://localhost:3000
echo.
pause
