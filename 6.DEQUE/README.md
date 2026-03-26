# 🟢 Leçon : DEQUE

---

## 1️⃣ Introduction aux listes en Python

En Python, **les listes** sont des structures de données permettant de stocker une collection d’éléments.
Il existe **différentes structures** selon les besoins :

| Structure                   | Nom Python       | Usage principal                               |
| --------------------------- | ---------------- | --------------------------------------------- |
| **Tableau** dynamique       | `list`           | Accès rapide par index, scripts généraux      |
| **Liste** double-ended      | `deque`          | Ajout/suppression rapide aux extrémités       |
| **Liste** chaînée classique | `Cons` (concept) | Algorithmique, théorie, langages fonctionnels |

---

## 2️⃣ `list` Python – tableau dynamique 📦

### Caractéristiques

* Implémentation **tableau dynamique contigu**
* Accès par index très rapide (`O(1)`)
* Ajout à la fin rapide (`append`)
* Insertion ou suppression au début lente (`O(n)`)
* Mémoire optimisée pour accès séquentiels

### Exemple

```python
my_list = [10, 20, 30, 40]
my_list.append(50)      # ajoute à la fin
my_list.insert(0, 5)    # ajoute au début (coûteux)
print(my_list)          # [5, 10, 20, 30, 40, 50]
```

### Schéma visuel

```
Index :   0       1       2       3
          ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐
list →    │ 10  │ │ 20  │ │ 30  │ │ 40  │
          └─────┘ └─────┘ └─────┘ └─────┘
```

💡 Astuce : **“list = Ligne contiguë”** → rapide pour accès index.

---

## 3️⃣ `deque` – Double-Ended Queue 🔵

### Pourquoi utiliser `deque` ?

* Avec une `list`, les **insertions au début** sont lentes
* `deque` permet des **ajouts et suppressions rapides** aux deux extrémités

### Exemple

```python
from collections import deque

dq = deque([10, 20, 30])
dq.append(40)      # ajout fin
dq.appendleft(5)   # ajout début
dq.pop()           # suppression fin
dq.popleft()       # suppression début
print(dq)          # deque([10, 20, 30])
```

### Schéma visuel

```
head
  |
  v
10 💎 <-> 20 💎 <-> 30 💎 <-> 40 💎
<-> double-ended = ajout/suppression début/fin rapide
```

💡 Astuce : **“deque = liste chaînée optimisée pour Python”**

---

## 4️⃣ `Cons` – Liste chaînée classique 🔴

### Concept

* Chaque **nœud** contient :

  * **valeur (`car`)**
  * **pointeur vers le suivant (`cdr`)**
* Accès par index lent (`O(n)`)
* Insertion début rapide (`O(1)`)
* Mémoire plus coûteuse (chaque nœud a un pointeur)

### Exemple en Python

```python
class Cons:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# Liste 1 -> 2 -> 3
l = Cons(1, Cons(2, Cons(3)))
# Accès
l.next.next.value
```

### Schéma visuel

```
head
  |
  v
1 💎 -> 2 💎 -> 3 💎 -> None
```

💡 Astuce : **“Cons = Chain of nodes”** → structure théorique, pas native Python.

---

## 5️⃣ Comparatif rapide

| 🔹 Caractéristique | 🟢 list           | 🔵 deque                  | 🔴 Cons                 |
| ------------------ | ---------------- | ------------------------- | ----------------------- |
| Accès par index    | ✅ O(1)           | ❌ O(n)                   | ❌ O(n)                 |
| Ajout à la fin     | ✅ O(1) amorti    | ✅ O(1)                   | ❌ O(n)                 |
| Ajout au début     | ❌ O(n)           | ✅ O(1)                   | ✅ O(1)                 |
| Suppression début  | ❌ O(n)           | ✅ O(1)                   | ✅ O(1)                 |
| Structure mémoire  | 📦 contiguë       | 🔗 nœuds liés optimisés   | 🔗 nœuds liés           |
| Usage réel         | Scripts généraux  | Files/Piles performantes | Algorithmique théorique |

---

## 6️⃣ Pourquoi Python n’a pas de `Cons` natif

* ✅ Les `list` couvrent la majorité des usages avec **simplicité et efficacité**
* ✅ `deque` couvre les cas d’**ajout/suppression aux extrémités**
* ❌ Liste chaînée classique = coûteuse en mémoire et rarement nécessaire en pratique
* ✅ Python privilégie **“batteries incluses” + lisibilité**

---

## 7️⃣ Mnémonique pour retenir

| Structure | Mnémotechnique                                                  |
| --------- | --------------------------------------------------------------- |
| `list`    | **L**igne contiguë → accès index rapide                         |
| `deque`   | **D**ouble-ended queue → rapide aux extrémités                  |
| `Cons`    | **C**hain of nodes → liste chaînée classique, concept théorique |

---

✅ **Résumé pédagogique**

* **`list`** : tableau dynamique, rapide accès index, append fin
* **`deque`** : liste double-ended optimisée, rapide aux extrémités
* **`Cons`** : concept de liste chaînée classique, rarement nécessaire en Python

## 8️⃣ Ensembles (`set`) 🔹

Un **ensemble** contient des **éléments uniques**, **non ordonnés**.

### Exemple

```python
s = {1, 2, 3}
s.add(3)   # déjà présent, ne sera pas ajouté
s.add(4)
print(s)
```

Résultat possible (ordre non garanti) :

```
{1, 2, 3, 4} ✅
```

### Opérations principales

| 🔹 Opération | 💻 Exemple    | ✨ Résultat    |                 |
| ------------ | ------------- | ------------- | --------------- |
| Ajouter      | `s.add(5)`    | `{1,2,3,4,5}` |                 |
| Supprimer    | `s.remove(2)` | `{1,3,4,5}`   |                 |
| Union        | `s            | {6,7}`        | `{1,3,4,5,6,7}` |
| Intersection | `s & {3,5,8}` | `{3,5}`       |                 |
| Différence   | `s - {4,7}`   | `{1,3,5}`     |                 |

💡 Idéal pour **unicité**, **intersection** et **union**.

---

## 9️⃣ Piles (`stack`) 🥞

Une **pile** fonctionne **LIFO (Last In First Out)**.

```
Top
⬆️ 30
⬆️ 20
⬆️ 10
Bottom
```

### Exemple Python

```python
pile = []
pile.append(10)  # push
pile.append(20)
pile.append(30)

print(pile.pop())  # 30 sort en premier
```

Résultat :

```
30
```

### Schéma Emoji

```
pile = []

push(10) -> 🟦10
push(20) -> 🟦20
push(30) -> 🟦30 (Top)

pop() -> retire 🟦30
```

💡 Utilité : **historique, DFS, undo**, etc.

---

## 1️⃣0️⃣ Comparaison rapide ⚡

| Structure               | Ordre            | Doublons        | Accès direct             | Usage typique                  |
| ----------------------- | ---------------- | --------------- | ------------------------ | ------------------------------ |
| 🔹 **Ensemble (`set`)** | ❌ Non ordonné    | ❌ Non autorisés | ❌ Non indexé             | Unicité, intersections, unions |
| 🥞 **Pile (`stack`)**   | ✅ Ordonné (LIFO) | ✅ Autorisés     | ✅ via `pop()`/`append()` | Historique, parcours DFS, undo |


