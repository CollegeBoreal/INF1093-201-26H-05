import matplotlib.pyplot as plt
import numpy as np

# --- Image 1 : Table de hachage ---
fig, ax = plt.subplots(figsize=(8, 4))
table = [[] for _ in range(5)]

def hash_simple(mot, taille):
    return sum(ord(c) for c in mot) % taille

data = [("alice", 25), ("bob", 30), ("charlie", 28), ("david", 40)]
for cle, val in data:
    table[hash_simple(cle, 5)].append(f"{cle}:{val}")

labels = [f"[{i}] {' | '.join(v) if v else 'vide'}" for i, v in enumerate(table)]
colors = ['lightcoral' if v else 'lightgray' for v in table]
ax.barh(range(5), [1]*5, color=colors, edgecolor='black')
for i, label in enumerate(labels):
    ax.text(0.05, i, label, va='center', fontsize=11)
ax.set_yticks([])
ax.set_xticks([])
ax.set_title('Table de hachage - Insertion', fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('images/hash_table.png')
plt.close()

# --- Image 2 : Compteur de mots ---
texte = "python est simple et python est puissant"
mots = texte.split()
compteur = {}
for mot in mots:
    compteur[mot] = compteur.get(mot, 0) + 1

fig, ax = plt.subplots(figsize=(8, 4))
ax.bar(compteur.keys(), compteur.values(), color='steelblue')
ax.set_title('Compteur de mots', fontsize=13, fontweight='bold')
ax.set_xlabel('Mots')
ax.set_ylabel('Occurrences')
plt.tight_layout()
plt.savefig('images/wordcount.png')
plt.close()

print("Images generees dans images/")