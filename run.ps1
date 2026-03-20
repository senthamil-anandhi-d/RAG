Write-Host "Starting PDF RAG System..." -ForegroundColor Cyan

# Start Backend in a new terminal window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd backend; .\venv\Scripts\activate; uvicorn main:app --host 0.0.0.0 --port 8000"

# Start Frontend in a new terminal window
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd frontend; npm run dev"

Write-Host "`nBackend starting at http://localhost:8000" -ForegroundColor Green
Write-Host "Frontend starting at http://localhost:3000" -ForegroundColor Green
Write-Host "Happy RAG-ing! 🎉" -ForegroundColor Yellow
