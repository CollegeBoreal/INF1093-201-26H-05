# Exercices

## 1️⃣ Graphe d’exemple

On représente le graphe avec un **dictionnaire Python** :

```python
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}
```

Structure du graphe :

```
      A
     / \
    B   C
   / \   \
  D   E   F
       \
        F
```

---

## 2️⃣ Algorithme DFS

Ton algorithme :

```python
def dfs(graph, start, visited=set()):
    visited.add(start)
    print(start, "🟢")
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
```

---

## 3️⃣ Exécution

On lance le parcours :

```python
dfs(graph, "A")
```

---

## 4️⃣ Ordre de visite

Le DFS va suivre **le premier chemin possible** :

```
A 🟢
B 🟢
D 🟢
E 🟢
F 🟢
C 🟢
```

---

## 5️⃣ Étapes du parcours

1. On commence à **A**
2. On va à **B**
3. On va à **D** (pas de voisins → retour)
4. Retour à **B**, puis **E**
5. **E → F**
6. Retour à **A**, puis **C**
7. **C → F** mais déjà visité

---

## 6️⃣ Version pédagogique (avec trace)

Pour montrer la récursion aux étudiants :

```python
def dfs(graph, start, visited=set(), depth=0):
    print("  " * depth + "Visite:", start)
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, depth + 1)
```

Sortie :

```
Visite: A
  Visite: B
    Visite: D
    Visite: E
      Visite: F
  Visite: C
```

On voit **la profondeur de la récursion**.

---

✅ **Idée clé à retenir**

DFS utilise :

* **la récursion** (ou une **pile / stack**)
* explore **un chemin complet avant les autres**

