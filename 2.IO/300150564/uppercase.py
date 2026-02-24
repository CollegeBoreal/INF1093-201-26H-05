with open("entree.txt", "r", encoding="utf-8") as f_in, open("sortie.txt", "w", encoding="utf-8") as f_out:
    for ligne in f_in:
        f_out.write(ligne.upper())

