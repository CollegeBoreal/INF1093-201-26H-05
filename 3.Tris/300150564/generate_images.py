import matplotlib.pyplot as plt

# --- Tri Insertion ---
avant = [8, 3, 5, 2, 9, 1]
apres = [1, 2, 3, 5, 8, 9]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.bar(range(len(avant)), avant, color='salmon')
ax1.set_title('Avant le tri')
ax1.set_xticks(range(len(avant)))
ax1.set_xticklabels(avant)
ax2.bar(range(len(apres)), apres, color='lightgreen')
ax2.set_title('Apres le tri')
ax2.set_xticks(range(len(apres)))
ax2.set_xticklabels(apres)
fig.suptitle('Tri par Insertion', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/tri_insertion.png')
plt.close()

# --- Tri Shell ---
avant = [45, 23, 11, 89, 77, 98, 4, 28, 65, 43]
apres = [4, 11, 23, 28, 43, 45, 65, 77, 89, 98]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.bar(range(len(avant)), avant, color='salmon')
ax1.set_title('Avant le tri')
ax2.bar(range(len(apres)), apres, color='lightgreen')
ax2.set_title('Apres le tri')
fig.suptitle('Tri de Shell', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/tri_shell.png')
plt.close()

# --- Tri Rapide ---
avant = [34, 7, 23, 32, 5, 62, 32, 2, 7]
apres = [2, 5, 7, 7, 23, 32, 32, 34, 62]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
ax1.bar(range(len(avant)), avant, color='salmon')
ax1.set_title('Avant le tri')
ax2.bar(range(len(apres)), apres, color='lightgreen')
ax2.set_title('Apres le tri')
fig.suptitle('Tri Rapide (Quick Sort)', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig('images/tri_quick.png')
plt.close()

print("Images generees dans images/")