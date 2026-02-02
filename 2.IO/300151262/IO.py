
# IO.py

f = open("etudiants.txt", "r")
lignes = f.readlines()
f.close()

total = 0
count = 0

out = open("resultats.txt", "w")
out.write("Étudiants avec note >= 60 :\n")

for ligne in lignes:
    nom, note = ligne.split()
    note = int(note)

    total += note
    count += 1

    if note >= 60:
        out.write(nom + " " + str(note) + "\n")

moyenne = total / count
out.write("\nMoyenne du groupe : " + str(round(moyenne, 2)))
out.close()

print("Traitement terminé.")
