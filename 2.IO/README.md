# 2️⃣ I/O (Input/Output)

## Traitement des entrées/sorties sur fichiers – Travail pratique (PowerShell + Python)

### Objectifs pédagogiques

À la fin de ce travail, l’étudiant.e sera capable de :

* Comprendre la différence entre entrée standard, sortie standard et erreur standard
* Lire et écrire dans des fichiers texte avec Python
* Traiter des fichiers ligne par ligne
* Rediriger des flux E/S avec PowerShell
* Automatiser un traitement simple sur des fichiers

---

## 1. Rappels théoriques

### 1.1 Les flux standards

* **STDIN** : entrée standard (clavier, pipe)
* **STDOUT** : sortie standard (console)
* **STDERR** : sortie d’erreur

### 1.2 Fichiers

* Un fichier est une suite de données persistantes
* Modes d’accès : lecture (`r`), écriture (`w`), ajout (`a`) en Python

---

## 2. Entrée / Sortie avec PowerShell (redirections)

### 2.1 Redirections

```powershell
# Écriture dans un fichier (remplace le contenu existant)
Get-Process > sortie.txt

# Ajout à un fichier existant
Get-Process >> sortie.txt

# Redirection des erreurs
Get-Process -Name NomInexistant 2> erreurs.txt
```

### 2.2 Pipes

```powershell
Get-Content erreurs.txt | Select-String "Cannot" | Measure-Object
```

---

## 3. Traitement de fichiers avec Python

### 3.1 Lecture ligne par ligne

```python
with open("fichier.txt", "r") as f:
    for ligne in f:
        print(f"Traitement: {ligne.strip()}")
```

### 3.2 Lecture et écriture

```python
with open("entree.txt", "r") as f_in, open("sortie.txt", "w") as f_out:
    for ligne in f_in:
        f_out.write(ligne.upper())
```

---

## 4. Travail pratique

### Contexte

Vous créez un fichier `etudiants.txt` contenant une liste d’étudiant.e.s et leurs notes.

**Exemple :**

```
Alice 85
Bob 62
Charlie 91
```

### Tâches à réaliser

1. Lire le fichier d’entrée avec Python
2. Calculer la moyenne
3. Générer un fichier `resultats.txt` contenant :

   * la liste des étudiant.e.s ayant ≥ 60
   * la moyenne du groupe
4. Rediriger les erreurs (fichier manquant, format invalide) avec PowerShell si besoin

### Contraintes

* Utilisation de **Python** pour le traitement
* Utilisation de **PowerShell** pour les redirections et tests de flux
* Script exécutable (`IO.py`)

---

## 5. Remise

* Script Python (`IO.py`)
* Fichiers d’entrée `etudiants.txt` et de sortie `resultats.txt`
* Court `README.md` expliquant le fonctionnement

---

💡 Astuce : testez vos scripts avec des fichiers vides et mal formés 😉
