@echo off
cd /d "%~dp0"
echo.
echo ======================================
echo   DEMARRAGE DU SERVEUR PORTNET HARPON
echo ======================================
echo.
echo Backend: http://127.0.0.1:8001
echo Documentation: http://127.0.0.1:8001/docs
echo.
venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
pause
