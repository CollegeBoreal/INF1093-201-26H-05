# 📊 TP I/O - Entrees/Sorties en Python – INF1093

**Nom :** Chouaib Ait Chouaib 🆔 300155045 **Date :** 06 avril 2026

---

## Devoir Python – Gestion des notes

Ce projet illustre le traitement des **entrées/sorties sur fichiers** en Python, combiné aux **redirections de flux** en PowerShell.

## Structure du répertoire

```
ID/
├── IO.py              ← Script principal Python
├── RAPPORT.ipynb      ← Rapport Jupyter Notebook avec diagrammes
├── etudiants.txt      ← Fichier d'entrée (données brutes)
├── entree.txt         ← Fichier d'entrée pour l'exercice 3.2
├── sortie.txt         ← Sortie en majuscules (exercice 3.2)
├── resultats.txt      ← Fichier de sortie généré automatiquement
├── README.md          ← Ce fichier
└── images/
    ├── .gitkeep
    └── diagramme_notes.png
```

## Fonctionnement

### IO.py

1. **Lecture** de `etudiants.txt` ligne par ligne
2. **Validation** du format (nom + note numérique)
3. **Calcul** de la moyenne du groupe
4. **Génération** de `resultats.txt` avec :
   - Liste des étudiants admis (note ≥ 60)
   - Liste des étudiants refusés
   - Moyenne du groupe
5. **Gestion des erreurs** vers STDERR (fichier manquant, format invalide)

### Exécution

```bash
# Exécution normale
python IO.py

# Avec redirections PowerShell
python IO.py > sortie_console.txt 2> erreurs.txt

# Test avec fichier manquant
python IO.py 2> erreurs.txt
```

## Format du fichier d'entrée

```
Alice 85
Bob 62
Charlie 91
```

Une ligne = un étudiant : `Prénom Note`

## Flux E/S

| Flux | Utilisation |
|------|-------------|
| STDIN | Lecture optionnelle depuis pipe |
| STDOUT | Résumé d'exécution en console |
| STDERR | Messages d'erreur et avertissements |

## Tests de robustesse

Le script gère :
- Fichier vide → 0 étudiants, pas d'erreur fatale
- Lignes vides → ignorées silencieusement
- Format invalide (note manquante ou non numérique) → avertissement STDERR
- Fichier inexistant → erreur STDERR + arrêt propre

## Diagramme

Le notebook `RAPPORT.ipynb` génère un diagramme en barres et un camembert des notes, sauvegardés dans `images/diagramme_notes.png`.

