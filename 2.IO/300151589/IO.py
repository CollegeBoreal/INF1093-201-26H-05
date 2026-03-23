with open("etudiants.txt", "r", encoding="utf-8") as f:
    lignes = f.readlines()

with open("resultats.txt", "w", encoding="utf-8") as f:
    for ligne in lignes:
        f.write(ligne)