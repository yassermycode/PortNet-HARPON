# 🧪 GUIDE DE TEST - Upload de documents

## ✅ CORRECTIONS APPLIQUÉES

### 1. **Synchronisation des ports**
- ✅ Frontend configuré sur `http://127.0.0.1:8001`
- ✅ Backend démarrera sur port `8001`
- ✅ Logs de débogage ajoutés dans `apiClient.js`
- ✅ Import `os` ajouté dans `main.py`

### 2. **Fichiers modifiés**
- `frontend/src/api/apiClient.js` - Ligne 3 : Port changé de 8000 → 8001
- `frontend/src/api/apiClient.js` - Lignes 47-49 : Logs de debug ajoutés
- `backend/app/main.py` - Ligne 6 : Import os ajouté
- `backend/app/main.py` - Ligne 54 : Message de démarrage mis à jour

---

## 🚀 COMMANDES DE DÉMARRAGE

### **Backend** (Terminal PowerShell)
```powershell
cd backend
.\start_backend.ps1
```

**OU manuellement :**
```powershell
cd backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

**Vérification :**
- ✅ Console affiche : "API prête sur http://127.0.0.1:8001"
- ✅ Ouvrir http://127.0.0.1:8001/docs → Voir la documentation Swagger

---

### **Frontend** (Terminal PowerShell)
```powershell
cd frontend
npm run dev
```

**Vérification :**
- ✅ Console affiche : "Local: http://localhost:5173"
- ✅ Ouvrir http://localhost:5173
- ✅ Console navigateur affiche : "🚀 API CLIENT LOADED - Backend: http://127.0.0.1:8001"

---

## 🧪 PROCÉDURE DE TEST

### **Étape 1 : Préparation**
1. Vider le cache du navigateur : `Ctrl+Shift+R` (Windows) ou `Cmd+Shift+R` (Mac)
2. Ouvrir la Console développeur : `F12` → Onglet "Console"
3. Garder les terminaux backend et frontend visibles

### **Étape 2 : Connexion**
1. Aller sur http://localhost:5173/login
2. Se connecter avec vos identifiants
3. Naviguer vers "Dossiers" → Sélectionner un dossier

### **Étape 3 : Upload de document**
1. Cliquer sur **"Uploader un document"**
2. Sélectionner un fichier PDF (exemple : facture, contrat)
3. Cliquer sur **"Uploader"**

### **Étape 4 : Vérifications**

#### **Dans la Console navigateur (F12)**, vous devriez voir :
```
📤 UPLOAD - Case ID: 1 | Fichier: test.pdf | Taille: 123456
📤 UPLOAD - URL complète: http://127.0.0.1:8001/api/v1/cases/1/documents
📤 REQUEST: POST http://127.0.0.1:8001/api/v1/cases/1/documents
✅ RESPONSE: 200 /api/v1/cases/1/documents
```

#### **Dans le terminal backend**, vous devriez voir :
```
============================================================
📤 UPLOAD DE DOCUMENT POUR LE DOSSIER 1
============================================================

🔵 Fichier: test.pdf
🔵 Type: application/pdf
💾 Sauvegarde dans: uploads/1/20260204_153045_test.pdf
✅ Fichier sauvegardé avec succès
🤖 LANCEMENT DE L'ANALYSE IA...
```

#### **Dans l'interface web**, vous devriez voir :
1. ✅ Popup : "Fichier uploadé avec succès !"
2. ✅ Le document apparaît dans la liste avec statut "ANALYZING" ou "ANALYZED"
3. ✅ Le score de risque est calculé et affiché
4. ✅ Les facteurs de risque sont listés

---

## 🐛 EN CAS D'ERREUR

### **Erreur : "Network Error" ou "ERR_CONNECTION_REFUSED"**
**Cause :** Le backend n'est pas démarré ou tourne sur le mauvais port

**Solution :**
```powershell
# Vérifier quel processus écoute sur le port 8001
netstat -ano | findstr :8001

# Si le port est occupé, tuer le processus
taskkill /PID <PID> /F

# Redémarrer le backend
cd backend
uvicorn app.main:app --reload --host 127.0.0.1 --port 8001
```

---

### **Erreur : "404 Not Found"**
**Cause :** La route n'est pas trouvée

**Solution :**
1. Vérifier que l'URL dans la console est exactement : `http://127.0.0.1:8001/api/v1/cases/{id}/documents`
2. Ouvrir http://127.0.0.1:8001/docs et chercher la route dans la documentation
3. Redémarrer le backend

---

### **Erreur : "CORS" ou "Access-Control-Allow-Origin"**
**Cause :** Le CORS n'autorise pas localhost:5173

**Solution :**
Vérifier que `backend/app/main.py` contient :
```python
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
```

---

### **Erreur : "File not found" ou "Permission denied"**
**Cause :** Le dossier `uploads/` n'existe pas ou n'a pas les permissions

**Solution :**
```powershell
cd backend
mkdir uploads
icacls uploads /grant Everyone:F
```

---

## ✅ RÉSULTAT ATTENDU FINAL

Après un upload réussi, vous devriez avoir :

1. **Dans `backend/uploads/{case_id}/`** : Le fichier PDF uploadé
2. **Dans la base de données** : 
   - Une entrée `Document` avec `status='ANALYZED'`
   - Un `risk_score` calculé (0-100)
   - Des `risk_factors` listés
3. **Dans l'interface** :
   - Le document visible avec icône PDF
   - Score de risque affiché (ex: 75/100)
   - Badge "✅ Analysé"
   - Liste des facteurs de risque
   - Recommandation affichée

---

## 📊 POINTS DE VÉRIFICATION

- [ ] Backend démarre sur port 8001
- [ ] Frontend charge et affiche "Backend: http://127.0.0.1:8001"
- [ ] Connexion réussie
- [ ] Dossier sélectionné
- [ ] Modal d'upload s'ouvre
- [ ] Fichier PDF sélectionné
- [ ] Upload lancé sans erreur
- [ ] Logs dans console navigateur OK
- [ ] Logs dans terminal backend OK
- [ ] Document apparaît dans la liste
- [ ] Analyse IA s'est exécutée
- [ ] Score de risque calculé et affiché

---

## 📞 AIDE SUPPLÉMENTAIRE

Si le problème persiste, fournissez :
1. Les logs complets de la console navigateur (F12)
2. Les logs complets du terminal backend
3. Une capture d'écran de l'erreur
4. Le résultat de : `netstat -ano | findstr :8001`
