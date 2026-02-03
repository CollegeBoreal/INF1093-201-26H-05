# 📊 Traitement des Entrées/Sorties – INF1093

**Auteur :** Maimouna Diallo 🆔 300155187  
**Date :** 02 février 2026  

---

## 1️⃣ Objectif
Lire un fichier contenant les noms et notes des étudiant·e·s, traiter les données, puis produire :  
- Un fichier de résultats (`resultats.txt`)  
- Un diagramme des notes  

---

## 2️⃣ Étapes principales

### a) Préparation du projet
1. Créer le dossier `2.IO/300155187`  
2. Ajouter un `README.md` et un dossier `images/`  
3. Placer les fichiers sources : `IO.py`, `etudiants.txt`  

---

### b) Lecture des données
```python
noms = []
notes = []

with open("etudiants.txt", "r") as f:
    for ligne in f:
        try:
            nom, note = ligne.split()
            noms.append(nom)
            notes.append(float(note))
        except ValueError:
            print("Ligne invalide :", ligne)

### c) Création d’un diagramme

```python
import matplotlib.pyplot as plt

plt.bar(noms, notes)
plt.xlabel("Étudiant.e.s")
plt.ylabel("Notes")
plt.title("Diagramme des notes")
plt.show()

### d) Gestion des fichiers et erreurs

**Rediriger les erreurs lors de l’exécution :**
```powershell
python IO.py 2> erreurs.txt


**Vérifier le contenu des erreurs :**
```powershell
Get-Content erreurs.txt


