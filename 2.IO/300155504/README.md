# 📂 Travail Pratique – I/O (INF1093)
**Étudiant :** 300155504

## Description

Ce projet démontre le traitement des entrées/sorties sur fichiers en Python, combiné avec des redirections PowerShell.

## Fichiers

| Fichier | Description |
|---|---|
| `IO.py` | Script principal Python |
| `RAPPORT.ipynb` | Notebook Jupyter avec diagramme |
| `etudiants.txt` | Fichier d'entrée (noms + notes) |
| `resultats.txt` | Fichier de sortie généré automatiquement |
| `entree.txt` | Fichier d'entrée pour test uppercase |
| `sortie.txt` | Résultat de la conversion en majuscules |
| `fichier.txt` | Fichier de test lecture ligne par ligne |
| `erreurs.txt` | Erreurs redirigées avec PowerShell |
| `erreurs_python.txt` | Erreurs capturées par Python |
| `uppercase.py` | Script de conversion en majuscules |
| `lecture_fichier.py` | Script de lecture ligne par ligne |

## Fonctionnement

1. Le script `IO.py` lit `etudiants.txt` ligne par ligne
2. Il filtre les étudiants ayant une note **≥ 60**
3. Il calcule la **moyenne du groupe**
4. Il écrit les résultats dans `resultats.txt`
5. Les erreurs sont redirigées vers `erreurs.txt`

## Exécution

### Python
```bash
python IO.py
```

### PowerShell (avec redirections)
```powershell
python IO.py
python IO.py 2> erreurs.txt
Get-Content erreurs.txt
```

## Gestion des erreurs

- Fichier introuvable → message d'erreur sur `stderr`
- Ligne mal formée → ligne ignorée + avertissement
- Note non numérique → ligne ignorée + avertissement
