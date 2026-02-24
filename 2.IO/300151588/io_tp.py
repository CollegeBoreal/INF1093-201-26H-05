# IO.py

input_file = "etudiants.txt"
output_file = "resultats.txt"

with open(input_file, "r", encoding="utf-8") as fin, \
     open(output_file, "w", encoding="utf-8") as fout:

    for line in fin:
        fout.write(line.strip().upper() + "\n")

print("Traitement terminé.")
