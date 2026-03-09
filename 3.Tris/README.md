# 📘 Algorithmes de tri – Tris variés (avec fichiers d’entrée)

[:tada: Participation](.scripts/Participation.md)

📍 Créer une page

 * créer un répertoire avec son 🆔 et ajouter le fichier README.md
 * créer un répertoire dans son répertoire 🆔, ajouter le répertoire images et ajouter le fichier .gitkeep
 * suivre les étapes ci-dessous dans votre répertoire 🆔

 ---

Les **tris classiques comme Insertion, Shell et Quick** sont **pensés pour des tableaux** (ou des structures à accès direct) pour plusieurs raisons :

---

## 🔹 1. Tri par insertion

* Besoin de **déplacer les éléments pour insérer une valeur**
* Avec un **tableau**, on peut accéder directement aux indices et décaler les éléments (`tab[j+1] = tab[j]`)
* complexité (cas moyen ou pire des cas) **O($n^2$)**
* Avec une **liste chaînée**, on pourrait faire l’insertion facilement, mais **le parcours pour trouver la bonne position devient séquentiel** → moins efficace

---

## 🔹 2. Tri de Shell

* Nécessite de **comparer et échanger des éléments espacés** à distance `écart`
* Accès direct indispensable (`tab[i - écart]`) → **tableau parfait pour ça**
* Complexité (cas moyen ou pire des cas), [séquence de Knuth](https://en.wikipedia.org/wiki/Shellsort) **O($n^{ \frac{3}{2} }$)**
* Liste chaînée → accès à un nœud éloigné = O(n) → beaucoup trop lent

---

## 🔹 3. Tri rapide (Quick Sort)

* Sépare le tableau en sous-parties autour d’un **pivot**
* Besoin d’**accès direct pour partitionner** les éléments
* Complexité (cas moyen ou pire des cas), **O(n log n)**
* Avec une liste chaînée, on peut l’adapter, mais la version tableau est beaucoup plus simple et rapide

---

## 🔹 Conclusion

| Algorithme | Structure recommandée | Pourquoi                                       |
| ---------- | --------------------- | ---------------------------------------------- |
| Insertion  | Tableau               | Déplacement rapide par indices                 |
| Shell      | Tableau               | Comparaisons espacées nécessitent accès direct |
| Quick      | Tableau               | Partition rapide via indices                   |

> **En pratique**, presque tous les cours utilisent **tableaux** pour ces tris classiques.
> Les listes chaînées sont plutôt utilisées pour des **inserts/suppressions rapides** ou des **structures dynamiques** (piles, files).

## 🎯 Objectif du travail

* Lire des données depuis un **fichier texte**
* Appliquer un **algorithme de tri**
* Afficher / vérifier le résultat

---

## 📂 Format commun des fichiers d’entrée

👉 Tous les fichiers auront **une liste d’entiers séparés par des espaces**

Exemple général :

```
8 3 5 2 9 1
```

---

# 🔹 1. Tri par insertion

## 📁 Fichier d’entrée

**`entree_insertion.txt`**

```
8 3 5 2 9 1
```

---

## 🧑‍💻 Lecture du fichier

```python
with open("entree_insertion.txt", "r") as f:
    tab = list(map(int, f.read().split()))
```

---

## 🧑‍💻 Algorithme

```python
PROCÉDURE tri_insertion(tab)
    POUR i ← 1 JUSQU’À longueur(tab) − 1 FAIRE
        clé ← tab[i]
        j ← i − 1

        TANT QUE j ≥ 0 ET tab[j] > clé FAIRE
            tab[j + 1] ← tab[j]
            j ← j − 1
        FIN TANT QUE

        tab[j + 1] ← clé
    FIN POUR
FIN PROCÉDURE
```

---

## ▶️ Programme principal

```python
tri_insertion(tab)
print("Résultat :", tab)
```

---

## 📌 Résultat attendu

```
Résultat : [1, 2, 3, 5, 8, 9]
```

---

# 🔹 2. Tri de Shell

## 📁 Fichier d’entrée

**`entree_shell.txt`**

```
45 23 11 89 77 98 4 28 65 43
```

---

## 🧑‍💻 Lecture du fichier

```python
with open("entree_shell.txt", "r") as f:
    tab = list(map(int, f.read().split()))
```

---

## 🧑‍💻 Algorithme

```python
PROCÉDURE tri_shell(tab)
    n ← longueur(tab)
    écart ← n ÷ 2

    TANT QUE écart > 0 FAIRE
        POUR i ← écart JUSQU’À n − 1 FAIRE
            temp ← tab[i]
            j ← i

            TANT QUE j ≥ écart ET tab[j − écart] > temp FAIRE
                tab[j] ← tab[j − écart]
                j ← j − écart
            FIN TANT QUE

            tab[j] ← temp
        FIN POUR

        écart ← écart ÷ 2
    FIN TANT QUE
FIN PROCÉDURE
```

---

## ▶️ Programme principal

```python
tri_shell(tab)
print("Résultat :", tab)
```

---

## 📌 Résultat attendu

```
Résultat : [4, 11, 23, 28, 43, 45, 65, 77, 89, 98]
```

---

# 🔹 3. Tri rapide (Quick Sort)

## 📁 Fichier d’entrée

**`entree_quick.txt`**

```
34 7 23 32 5 62 32 2 7
```

---

## 🧑‍💻 Lecture du fichier

```python
with open("entree_quick.txt", "r") as f:
    tab = list(map(int, f.read().split()))
```

---

## 🧑‍💻 Algorithme

```python
PROCÉDURE tri_rapide(tab)
    SI longueur(tab) ≤ 1 ALORS
        RETOURNER tab
    FIN SI

    pivot ← tab[longueur(tab) ÷ 2]

    gauche ← liste vide
    milieu ← liste vide
    droite ← liste vide

    POUR chaque élément x DANS tab FAIRE
        SI x < pivot ALORS
            ajouter x à gauche
        SINON SI x = pivot ALORS
            ajouter x à milieu
        SINON
            ajouter x à droite
        FIN SI
    FIN POUR

    RETOURNER concaténer(
        tri_rapide(gauche),
        milieu,
        tri_rapide(droite)
    )
FIN PROCÉDURE
```

---

## ▶️ Programme principal

```python
tab_trie = tri_rapide(tab)
print("Résultat :", tab_trie)
```

---

## 📌 Résultat attendu

```
Résultat : [2, 5, 7, 7, 23, 32, 32, 34, 62]
```

---

# 📌 Conclusion pédagogique

> Le **fichier d’entrée permet de séparer les données de l’algorithme**,
> exactement comme dans un vrai programme professionnel.


On va créer une **structure de répertoire claire** pour tes trois exercices de tri et fournir **les fichiers Python et fichiers d’entrée** pour chaque exercice.

---

## 📂 Structure de répertoires

```
ID/
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
