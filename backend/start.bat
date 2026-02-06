@echo off
cd /d "C:\Users\pc\Desktop\PortNet-HARPON\PortNet-HARPON\backend"
echo Demarrage du backend HARPON...
"C:\Users\pc\Desktop\PortNet-HARPON\.venv\Scripts\uvicorn.exe" app.main:app --host 127.0.0.1 --port 8001
pause
