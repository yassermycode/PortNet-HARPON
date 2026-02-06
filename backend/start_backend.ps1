# Script de démarrage du backend PortNet-HARPON
# Port: 8001

Write-Host "🚀 Démarrage du backend PortNet-HARPON..." -ForegroundColor Cyan
Write-Host "📍 Port: 8001" -ForegroundColor Yellow
Write-Host ""

# Vérifier que le dossier uploads existe
if (-not (Test-Path "uploads")) {
    New-Item -ItemType Directory -Path "uploads" | Out-Null
    Write-Host "✅ Dossier 'uploads' créé" -ForegroundColor Green
}

# Démarrer uvicorn
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
