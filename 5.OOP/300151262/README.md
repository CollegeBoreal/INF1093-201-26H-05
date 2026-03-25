# Projet Python — Formes Géométriques

**Étudiant :** Ahmed BERGUI
**Répertoire :** `8.OOP/300151262`

## Structure du projet

```text
ahmed.bergui/
├── README.md
├── images/
│   └── .gitkeep
├── main.py
├── figure.py
├── Carre.py
├── Cercle.py
├── Triangle.py
├── Cube.py
├── requirements.txt
└── RAPPORT.ipynb
```

## Description

Ce projet démontre les bases de la programmation orientée objet en Python à l’aide de figures géométriques :

- `Figure` : classe de base
- `Carre` : classe dérivée
- `Cercle` : classe dérivée
- `Triangle` : extension demandée dans l’exercice
- `Cube` : extension supplémentaire en 3D

Le fichier `main.py` crée plusieurs formes, affiche leurs informations et montre un exemple simple de polymorphisme.

## Exécution

```bash
python3 main.py
```

## Dépendances graphiques

```bash
python3 -m pip install -r requirements.txt
```

## Jupyter

Pour ouvrir le notebook :

```bash
jupyter lab
```

Puis ouvrir `RAPPORT.ipynb`.

## Git / GitHub

Depuis le dossier parent de votre identifiant :

```bash
git add ahmed.bergui
git commit -m "ajout du cube"
git push
```

## Note technique

Sous Linux, les noms de fichiers sont sensibles à la casse. Les imports utilisent donc :

```python
from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle
from Cube import Cube
```
