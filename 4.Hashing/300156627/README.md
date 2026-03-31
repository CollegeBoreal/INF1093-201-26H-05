PROJET DE Hashing

🧠 Leçon : Hashing et Dictionnaires en Python

🎯 Objectifs
À la fin de cette leçon, tu seras capable de :

Expliquer ce qu’est le hashing.
Comprendre comment un dictionnaire Python fonctionne.
Utiliser un dictionnaire pour stocker, accéder et modifier des données.
Comprendre pourquoi un dictionnaire est rapide.

Qu’est‑ce que le Hashing ?
👉 Définition simple
Le hashing est un procédé qui transforme une donnée (texte, nombre…) en une valeur numérique appelée hash.

Exemple :

Le mot "chat" → 4872309847
Le mot "chien" → 8293029832
Cette valeur :

est générée automatiquement,
est unique dans la plupart des cas,
sert à retrouver les données très rapidement.
🧪 Exemple : la fonction hash() en Python
print(hash("chat"))
print(hash("chien"))
👉 Tu verras apparaître deux grands nombres différents.

📌 Rôle du hashing
Il sert à :

ranger des données dans des “cases” en mémoire,
retrouver ces données très vite.
2. 📚 Les dictionnaires en Python
Un dictionnaire (dict) est une structure qui stocke des informations sous forme :
clé → valeur

Exemples de paires clé/valeur :

"nom" → "Alice"
"âge" → 15
"note" → 92.5
📝 Exemple de dictionnaire
eleve = {
    "nom": "Alice",
    "age": 15,
    "classe": "Secondaire 3"
}
3. 🧩 Comment un dictionnaire fonctionne
Même si Python te montre quelque chose de simple, à l’intérieur, lorsque tu écris :

eleve["nom"]
Python fait ceci :

Prendre la clé "nom".
Calculer son hash (un nombre).
Aller directement à l’endroit mémoire correspondant.
Ramener la valeur "Alice".
🎉 Résultat :
Presque instantané, même si le dictionnaire contient 1 million d’éléments.