# Script pour démarrer le serveur backend
Write-Host "🚀 Démarrage du serveur PortNet HARPON..." -ForegroundColor Cyan

# Se placer dans le dossier backend
Set-Location $PSScriptRoot

# Activer l'environnement virtuel et démarrer uvicorn
& ".\venv\Scripts\python.exe" -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
