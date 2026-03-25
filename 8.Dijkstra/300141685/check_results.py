# INF1093 - Programmation 2 - Dijkstra
# Souleymane Barry - 300141685
# Fichier: check_results.py

from dijkstra_tp import shortest, g, target

path = shortest(target)
expected_path = ['a', 'c', 'f', 'e']

print("=" * 50)
print("VERIFICATION DES RESULTATS")
print("=" * 50)
print(f"Votre chemin: {path}")
print(f"Chemin attendu: {expected_path}")

if path == expected_path:
    print("\n✅ BRAVO ! Le chemin est correct.")
    print(f"Le plus court chemin: {' -> '.join(path)}")
else:
    print("\n❌ Chemin incorrect.")

print("\n" + "=" * 50)
print("DISTANCES FINALES")
print("=" * 50)
for v in g:
    print(f"Distance de a a {v.get_id()}: {v.get_distance()}")
