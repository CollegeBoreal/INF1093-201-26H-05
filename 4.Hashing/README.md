# 🧠 Leçon : Hashing et Dictionnaires en Python

## 🎯 Objectifs

À la fin de cette leçon, tu seras capable de :

*   Expliquer ce qu’est le **hashing**.
*   Comprendre comment un **dictionnaire Python** fonctionne.
*   Utiliser un dictionnaire pour stocker, accéder et modifier des données.
*   Comprendre pourquoi un dictionnaire est **rapide**.

***

# 1. 🔐 Qu’est‑ce que le Hashing ?

### 👉 Définition simple

Le **hashing** est un procédé qui transforme une donnée (texte, nombre…) en une **valeur numérique** appelée *hash*.

Exemple :

*   Le mot `"chat"` → 4872309847
*   Le mot `"chien"` → 8293029832

Cette valeur :

*   est générée automatiquement,
*   est unique dans la plupart des cas,
*   sert à retrouver les données **très rapidement**.

### 🧪 Exemple : la fonction `hash()` en Python

```python
print(hash("chat"))
print(hash("chien"))
```

👉 Tu verras apparaître deux grands nombres différents.

### 📌 Rôle du hashing

Il sert à :

*   ranger des données dans des “cases” en mémoire,
*   retrouver ces données très vite.

***

# 2. 📚 Les dictionnaires en Python

Un **dictionnaire** (`dict`) est une structure qui stocke des informations sous forme :  
**clé → valeur**

Exemples de paires clé/valeur :

*   `"nom"` → `"Alice"`
*   `"âge"` → `15`
*   `"note"` → `92.5`

### 📝 Exemple de dictionnaire

```python
eleve = {
    "nom": "Alice",
    "age": 15,
    "classe": "Secondaire 3"
}
```

***

# 3. 🧩 Comment un dictionnaire fonctionne

Même si Python te montre quelque chose de simple, **à l’intérieur**, lorsque tu écris :

```python
eleve["nom"]
```

Python fait ceci :

1.  Prendre la clé `"nom"`.
2.  Calculer son **hash** (un nombre).
3.  Aller directement à l’endroit mémoire correspondant.
4.  Ramener la valeur `"Alice"`.

🎉 Résultat :  
**Presque instantané**, même si le dictionnaire contient 1 million d’éléments.

***

# 4. 🗂️ Pourquoi un dictionnaire est rapide ?

Grâce au hashing !  
→ Pas besoin de parcourir toute la liste.  
→ Python “sait” directement où chercher.

C’est comme :

*   Une bibliothèque sans hashing : tu cherches livre par livre.
*   Une bibliothèque **avec hashing** : chaque livre a une adresse exacte.

***

# 5. 🛠️ Utiliser un dictionnaire en Python

## ✔️ Créer un dictionnaire

```python
personne = {
    "nom": "Khaled",
    "age": 16
}
```

## ✔️ Lire une valeur

```python
print(personne["nom"])  # Affiche Khaled
```

## ✔️ Modifier une valeur

```python
personne["age"] = 17
```

## ✔️ Ajouter une nouvelle clé

```python
personne["ville"] = "Mississauga"
```

## ✔️ Supprimer une clé

```python
del personne["age"]
```

***

# 6. 🔎 Exemple complet

Imaginons un mini carnet de notes :

```python
notes = {
    "INF1042": 89,
    "INF1093": 92,
    "INF1083": 78
}

# Récupérer une note
print(notes["INF1093"])

# Changer une note
notes["INF1083"] = 85

# Ajouter un cours
notes["INF1103"] = 90

print(notes)
```

***

# 7. 🧠 Pourquoi ne pas utiliser une liste ?

### Liste

```python
notes = [("INF1042", 89), ("INF1103", 92)]
```

Si tu veux trouver `"INF1103"`, tu dois regarder chaque élément → lent.

```python
for c, v in notes: print(c, v, "→ trouvé" if c == "INF1103" else "")
```

### Dictionnaire

```python
notes = {"INF1042": 89, "INF1103": 92}
```

Accès direct → rapide.

```python
notes['INF1042']
```

***

# 8. 🏁 Résumé

| Concept      | Explication                                                   |
| ------------ | ------------------------------------------------------------- |
| Hashing      | Transformer une donnée en nombre pour la retrouver rapidement |
| Dictionnaire | Structure clé → valeur                                        |
| Avantage     | Accès très rapide                                             |
| Utilisation  | Stockage de données organisées                                |

***

