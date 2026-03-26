import os

texte = "python est simple et python est puissant"
mots = texte.split()  

compte = {}

for m in mots:
    if m in compte:
        compte[m] += 1 
    else:
        compte[m] = 1   
os.makedirs("resultats", exist_ok=True)
with open("resultats/ex5.txt", "w") as f:
    for mot, nb in compte.items():
        f.write(f"{mot}:{nb}\n")
        print(f"Statistique : '{mot}' apparaît {nb} fois")
