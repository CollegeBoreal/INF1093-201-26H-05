# uppercase.py - Convertit le contenu de entree.txt en majuscules dans sortie.txt

with open("entree.txt", "r") as f_in, open("sortie.txt", "w") as f_out:
    for ligne in f_in:
        f_out.write(ligne.upper())

print("Conversion en majuscules terminée. Résultat dans sortie.txt")
