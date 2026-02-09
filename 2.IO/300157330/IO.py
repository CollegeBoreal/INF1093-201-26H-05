
# IO_employes.py

f = open("employes.txt", "r")
lignes = f.readlines()
f.close()

total = 0
count = 0

out = open("rapport.txt", "w")
out.write("Employés avec salaire >= 6000 :\n")

for ligne in lignes:
    nom, salaire = ligne.split()
    salaire = int(salaire)

    total += salaire
    count += 1

    if salaire >= 6000:
        out.write(nom + " " + str(salaire) + "\n")

moyenne = total / count
out.write("\nSalaire moyen : " + str(round(moyenne, 2)))
out.close()

print("Traitement terminé.")
