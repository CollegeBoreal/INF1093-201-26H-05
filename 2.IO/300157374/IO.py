# Lire le fichier entree.txt
with open("entree.txt", "r", encoding="utf-8") as f:
    contenu = f.read()

# Transformer en majuscule
resultat = contenu.upper()

# Écrire dans sortie.txt
with open("sortie.txt", "w", encoding="utf-8") as f:
    f.write(resultat)

# Écrire dans resultats.txt
with open("resultats.txt", "w", encoding="utf-8") as f:
    f.write("Traitement terminé\n")
    f.write(resultat)
