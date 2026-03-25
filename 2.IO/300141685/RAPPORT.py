# INF1093 - Programmation 2
# Traitement I/O (Input/Output)
# Nom: Souleymane Barry
# ID: 300141685

import matplotlib.pyplot as plt

noms = []
notes = []

# Lecture du fichier etudiants.txt
with open("etudiants.txt", "r", encoding="utf-8") as fichier:
    for ligne in fichier:
        ligne = ligne.strip()
        if ligne:  # Ignorer les lignes vides
            donnees = ligne.split(",")
            nom = donnees[0]
            note = float(donnees[1])
            noms.append(nom)
            notes.append(note)

# Calcul de la moyenne
moyenne = sum(notes) / len(notes)

# Creation du graphique
plt.figure(figsize=(10, 5))
plt.bar(noms, notes, color='lightgreen')
plt.axhline(moyenne, color='red', linestyle='--', linewidth=2, label=f'Moyenne: {moyenne:.2f}')
plt.title("Notes des etudiant.e.s")
plt.xlabel("Etudiant.e.s")
plt.ylabel("Notes")
plt.legend()
plt.show()