@echo off
cd /d "%~dp0"
echo ========================================
echo  HARPON Backend - Demarrage
echo ========================================
echo.
echo Repertoire: %CD%
echo.
C:\Users\pc\Desktop\PortNet-HARPON\.venv\Scripts\uvicorn.exe app.main:app --host 127.0.0.1 --port 8001
pause
