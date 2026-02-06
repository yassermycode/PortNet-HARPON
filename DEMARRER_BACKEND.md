# 🚀 INSTRUCTIONS POUR DÉMARRER LE BACKEND

## Problème résolu
✅ Routes corrigées : POST /api/v1/cases/{case_id}/documents
✅ CORS configuré en mode permissif
✅ Header Content-Type corrigé pour FormData
✅ Logs détaillés ajoutés

## Pour démarrer le backend :

### Option 1 : Script Batch (RECOMMANDÉ)
1. Double-cliquez sur : `backend/START_BACKEND.bat`
2. Le serveur démarre automatiquement
3. Ne fermez PAS la fenêtre !

### Option 2 : Terminal VS Code
1. Ouvrez un nouveau terminal PowerShell dans VS Code
2. Exécutez :
```powershell
cd C:\Users\pc\Desktop\PortNet-HARPON\PortNet-HARPON\backend
.\venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8001 --reload
```
3. Laissez le terminal ouvert

### Option 3 : Script PowerShell
```powershell
cd C:\Users\pc\Desktop\PortNet-HARPON\PortNet-HARPON\backend
.\start_server.ps1
```

## Vérification
Une fois démarré, vous devriez voir :
```
✅ API prête sur http://127.0.0.1:8001
📚 Documentation sur http://127.0.0.1:8001/docs
```

Testez dans le navigateur : http://127.0.0.1:8001/health
(Vous devriez voir : `{"status":"healthy"}`)

## Ensuite : Tester l'upload
1. Assurez-vous que le frontend tourne sur http://localhost:5173
2. Allez dans un dossier (case)
3. Cliquez sur "Uploader un document"
4. Sélectionnez un fichier PDF
5. Regardez la console du navigateur pour les logs détaillés

Si vous voyez toujours une erreur, copiez TOUS les messages de la console (F12).
