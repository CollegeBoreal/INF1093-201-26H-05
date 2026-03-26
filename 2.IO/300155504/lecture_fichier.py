# lecture_fichier.py - Lecture ligne par ligne d'un fichier texte

with open("fichier.txt", "r") as f:
    for ligne in f:
        print(f"Traitement: {ligne.strip()}")
