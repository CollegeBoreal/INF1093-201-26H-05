Parfait 👍
Je reprends **la leçon sur les tris (Insertion, Shell, Quick)** en ajoutant **pour CHAQUE algorithme un fichier d’entrée** clair et réaliste, comme demandé pour un **travail pratique Python**.

---

# 📘 Algorithmes de tri – Tris variés (avec fichiers d’entrée)

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
def tri_insertion(tab):
    for i in range(1, len(tab)):
        cle = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > cle:
            tab[j + 1] = tab[j]
            j -= 1
        tab[j + 1] = cle
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
def tri_shell(tab):
    n = len(tab)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = tab[i]
            j = i
            while j >= gap and tab[j - gap] > temp:
                tab[j] = tab[j - gap]
                j -= gap
            tab[j] = temp
        gap //= 2
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
def tri_rapide(tab):
    if len(tab) <= 1:
        return tab
    pivot = tab[len(tab) // 2]
    gauche = [x for x in tab if x < pivot]
    milieu = [x for x in tab if x == pivot]
    droite = [x for x in tab if x > pivot]
    return tri_rapide(gauche) + milieu + tri_rapide(droite)
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

# 🧪 Extension (option TP)

👉 Modifier les fichiers pour tester :

* liste déjà triée
* liste inversée
* très grande liste (1000 nombres)
* doublons nombreux

---

# 📌 Conclusion pédagogique

> Le **fichier d’entrée permet de séparer les données de l’algorithme**,
> exactement comme dans un vrai programme professionnel.

