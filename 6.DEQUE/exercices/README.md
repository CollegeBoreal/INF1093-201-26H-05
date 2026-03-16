# 📚 Leçon — Structures de données linéaires en Python

## Listes, piles, files et `deque`

---

# 1️⃣ Introduction

Une **structure de données** est une manière d’organiser les données en mémoire afin de :

* 📦 les **stocker**
* 🔎 les **accéder**
* ✏️ les **modifier**
* ⚡ les **traiter efficacement**

En Python, plusieurs structures existent :

| Structure | Type              | Usage                  |
| --------- | ----------------- | ---------------------- |
| `list`    | tableau dynamique | usage général          |
| `deque`   | file double       | file et pile efficaces |
| `set`     | ensemble          | éliminer les doublons  |
| `dict`    | table de hachage  | clé → valeur           |

Dans cette leçon nous étudierons :

* 📋 **list**
* 🥞 **pile (stack)**
* 🚶 **file (queue)**
* ↔️ **deque**

---

# 2️⃣ Les listes (`list`)

Une **liste Python** est un **tableau dynamique**.

```python
tab = [3, 7, 2, 9]
```

---

## 🔧 Opérations principales

| opération   | code       |
| ----------- | ---------- |
| ➕ ajouter   | `append()` |
| ➖ supprimer | `pop()`    |
| 🔎 accéder  | `tab[i]`   |
| 📏 longueur | `len(tab)` |

---

## 🧪 Exemple

```python
tab = [10, 20, 30]

tab.append(40)

print(tab)
```

Résultat

```
[10, 20, 30, 40]
```

---

## ⚡ Complexité

| opération       | complexité  |
| --------------- | ----------- |
| accès           | O(1)        |
| append          | O(1) amorti |
| insertion début | O(n)        |

⚠️ Problème : insérer **au début** d'une liste est **lent**.

---

# 3️⃣ Pile (Stack)

Une **pile** fonctionne selon le principe :

📦 **LIFO — Last In First Out**

Exemple réel :

🥞 pile d'assiettes

```
   5
   4
   3
```

On retire **toujours le dernier élément ajouté**.

---

## 🧑💻 Implémentation avec `list`

```python
pile = []

pile.append(10)
pile.append(20)
pile.append(30)

print(pile.pop())
```

Résultat

```
30
```

---

## 📊 Schéma

```
push(10)
push(20)
push(30)

pile = [10,20,30]

pop() -> 30
```

---

# 4️⃣ File (Queue)

Une **file** fonctionne selon :

🚶 **FIFO — First In First Out**

Exemple :

file d'attente à la banque.

```
A -> B -> C
```

A sortira en premier.

---

## ⚠️ Implémentation naïve avec `list`

```python
file = []

file.append("A")
file.append("B")
file.append("C")

file.pop(0)
```

⚠️ `pop(0)` est **O(n)** car tous les éléments sont déplacés.

---

# 5️⃣ `deque` (double ended queue)

Python fournit une structure optimisée :

```python
from collections import deque
```

`deque` signifie :

↔️ **double ended queue**

On peut ajouter ou retirer **des deux côtés**.

---

## 🏗 Création

```python
from collections import deque

d = deque()
```

---

## ➕ Ajouter des éléments

```python
d.append(10)
d.append(20)
d.append(30)
```

```
[10,20,30]
```

---

## ➖ Retirer à droite

```python
d.pop()
```

---

## ⬅️ Retirer à gauche

```python
d.popleft()
```

---

## ➕ Ajouter au début

```python
d.appendleft(5)
```

---

## 🧪 Exemple complet

```python
from collections import deque

file = deque()

file.append("A")
file.append("B")
file.append("C")

print(file.popleft())
print(file.popleft())
```

Résultat

```
A
B
```

---

# 6️⃣ ⚡ Complexité de `deque`

| opération  | complexité |
| ---------- | ---------- |
| append     | O(1)       |
| appendleft | O(1)       |
| pop        | O(1)       |
| popleft    | O(1)       |

💡 Donc `deque` est **idéal pour les files et piles**.

---

# 7️⃣ 📊 Comparaison `list` vs `deque`

| opération  | list | deque |
| ---------- | ---- | ----- |
| append     | O(1) | O(1)  |
| pop        | O(1) | O(1)  |
| pop(0)     | O(n) | O(1)  |
| appendleft | O(n) | O(1)  |

🎯 Conclusion :

```
list  -> tableau
deque -> file / pile
```

---

# 8️⃣ 💻 Exemple réel : simulation d'une file

```python
from collections import deque

file = deque()

file.append("client1")
file.append("client2")
file.append("client3")

while file:
    client = file.popleft()
    print("Service :", client)
```

Sortie

```
Service : client1
Service : client2
Service : client3
```

---

# 9️⃣ 🧪 Exercices

---

## 🥞 Exercice 1 — Pile

Créer une pile qui :

1️⃣ ajoute **5 nombres**
2️⃣ retire les nombres un par un
3️⃣ les affiche

---

## 🚶 Exercice 2 — File

Créer une file avec `deque` :

```
Alice
Bob
Charlie
```

Puis afficher l'ordre de sortie.

---

## 🔄 Exercice 3 — Inversion avec une pile

Écrire un programme qui inverse une chaîne :

```
bonjour
```

Résultat attendu

```
ruojnob
```

💡 Indice : utiliser une **pile**.

---

## 🖨 Exercice 4 — Simulation file d'impression

Simuler une **file d'imprimante** :

documents :

```
doc1
doc2
doc3
doc4
```

Chaque document est imprimé dans l'ordre.

---

# 🔟 Bonus — `deque` avancé

## 📏 Limiter la taille

```python
d = deque(maxlen=3)

d.append(1)
d.append(2)
d.append(3)
d.append(4)

print(d)
```

Résultat

```
[2,3,4]
```

🧠 Le plus ancien élément est supprimé automatiquement.

---

# 🧾 1️⃣   Résumé

| structure | usage               |
| --------- | ------------------- |
| 📋 list   | tableau             |
| 🥞 pile   | LIFO                |
| 🚶 file   | FIFO                |
| ↔️ deque  | file/pile optimisée |

---

✅ **Points clés**

* `list` = tableau dynamique 📋
* `deque` = structure rapide pour files et piles ⚡
* `deque` évite les coûts **O(n)**

