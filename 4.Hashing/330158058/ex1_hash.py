def calcul_hash(texte, taille_table):
    somme = 0
    for caractere in texte:
        somme += ord(caractere)
    return somme % taille_table


elements = ["reseau", "python", "serveur", "client"]
taille = 12

with open("resultats/ex1.txt", "w", encoding="utf-8") as fichier:
    for element in elements:
        position = calcul_hash(element, taille)
        fichier.write(f"{element} -> case {position}\n")
