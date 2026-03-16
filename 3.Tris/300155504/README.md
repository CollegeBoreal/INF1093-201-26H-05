# 📘 Algorithmes de tri – Tris variés (avec fichiers d'entrée)
**Étudiant :** Badreddine Barragoub  
**ID :** 300155504  
**Cours :** INF1093 – Structures de données et fichiers  
**Projet :** Implémentation de différents algorithmes de tri en Python

---

## 🎯 Objectif du projet
Ce projet a pour objectif de lire des données à partir de fichiers texte, d'appliquer différents algorithmes de tri et d'afficher les résultats triés.
Les données d'entrée sont séparées des programmes afin de reproduire une approche utilisée dans les projets informatiques professionnels.

---

## 🧠 Algorithmes de tri utilisés
Trois algorithmes de tri classiques ont été implémentés :
- **Tri par insertion** : insère chaque élément à sa position correcte dans la partie déjà triée du tableau.  
- **Tri de Shell** : amélioration du tri par insertion en comparant des éléments espacés.  
- **Tri rapide (Quick Sort)** : divise les données autour d'un pivot et trie récursivement les sous-parties.

Ces algorithmes sont généralement appliqués sur des **tableaux**, car ils nécessitent un accès direct aux indices pour être efficaces.

---

## 📂 Structure du projet
```
300155504/
│
├─ insertion/
│   ├─ main.py
│   └─ entree_insertion.txt
│
├─ shell/
│   ├─ main.py
│   └─ entree_shell.txt
│
└─ quick/
    ├─ main.py
    └─ entree_quick.txt
```

Chaque dossier contient :
- un **programme Python** qui implémente l'algorithme
- un **fichier d'entrée** contenant les nombres à trier

---

## 📄 Format des fichiers d'entrée
Les fichiers contiennent simplement des entiers séparés par des espaces.
Exemple :
```
10 1 11 2 12 3 13 4 14 5 15 6 16 7 17 8 18 9 19 0
```

---

## ▶️ Exemple de résultat
```
Résultat : [1, 2, 3, 5, 8, 9]
```

---

## 📌 Conclusion
Ce projet permet de comprendre le fonctionnement de plusieurs algorithmes de tri et l'utilisation des fichiers d'entrée pour séparer les données du code. Cette approche facilite la réutilisation et l'organisation des programmes.
