chaine = "le chat dort et le chien joue avec le chat"

elements = chaine.split()

resultat = {}

for element in set(elements):
    total = elements.count(element)
    resultat[element] = total

with open("resultats/ex5.txt", "w") as fichier:
    for element in resultat:
        fichier.write(element + " = " + str(resultat[element]) + "\n")
