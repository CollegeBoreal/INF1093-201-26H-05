import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 4, figsize=(16, 8))
fig.suptitle('Figures Geometriques - POO Python', fontsize=16, fontweight='bold')

# Carre
ax = axes[0][0]
cote = 4
x = [0, cote, cote, 0, 0]
y = [0, 0, cote, cote, 0]
ax.plot(x, y, 'b-', linewidth=2)
ax.fill(x, y, alpha=0.3, color='blue')
ax.set_title(f'Carre\naire={cote**2}')
ax.axis('equal')
ax.grid(True)

# Cercle
ax = axes[0][1]
r = 3
theta = np.linspace(0, 2*np.pi, 300)
ax.plot(r*np.cos(theta), r*np.sin(theta), 'r-', linewidth=2)
ax.fill(r*np.cos(theta), r*np.sin(theta), alpha=0.3, color='red')
ax.set_title(f'Cercle\naire={3.14159*r**2:.2f}')
ax.axis('equal')
ax.grid(True)

# Triangle
ax = axes[0][2]
b, h = 5, 2
x = [0, b, b/2, 0]
y = [0, 0, h, 0]
ax.plot(x, y, 'g-', linewidth=2)
ax.fill(x, y, alpha=0.3, color='green')
ax.set_title(f'Triangle\naire={b*h/2}')
ax.axis('equal')
ax.grid(True)

# Losange
ax = axes[0][3]
d1, d2 = 6, 4
x = [0, d1/2, 0, -d1/2, 0]
y = [d2/2, 0, -d2/2, 0, d2/2]
ax.plot(x, y, color='orange', linewidth=2)
ax.fill(x, y, alpha=0.3, color='orange')
ax.set_title(f'Losange\naire={d1*d2/2}')
ax.axis('equal')
ax.grid(True)

# Rectangle
ax = axes[1][0]
l, h = 5, 3
x = [0, l, l, 0, 0]
y = [0, 0, h, h, 0]
ax.plot(x, y, color='purple', linewidth=2)
ax.fill(x, y, alpha=0.3, color='purple')
ax.set_title(f'Rectangle\naire={l*h}')
ax.axis('equal')
ax.grid(True)

# Pentagone
ax = axes[1][1]
n, r = 5, 4
angles = [2*np.pi*i/n - np.pi/2 for i in range(n+1)]
x = [r*np.cos(a) for a in angles]
y = [r*np.sin(a) for a in angles]
ax.plot(x, y, color='brown', linewidth=2)
ax.fill(x, y, alpha=0.3, color='brown')
ax.set_title(f'Pentagone\naire=27.53')
ax.axis('equal')
ax.grid(True)

# Etoile
ax = axes[1][2]
r_ext, r_int = 5, 2
angles_ext = [2*np.pi*i/5 - np.pi/2 for i in range(6)]
angles_int = [2*np.pi*i/5 - np.pi/2 + np.pi/5 for i in range(6)]
x, y = [], []
for i in range(5):
    x += [r_ext*np.cos(angles_ext[i]), r_int*np.cos(angles_int[i])]
    y += [r_ext*np.sin(angles_ext[i]), r_int*np.sin(angles_int[i])]
x.append(x[0])
y.append(y[0])
ax.plot(x, y, color='gold', linewidth=2)
ax.fill(x, y, alpha=0.3, color='gold')
ax.set_title(f'Etoile\naire=30.78')
ax.axis('equal')
ax.grid(True)

# Vide
axes[1][3].axis('off')

plt.tight_layout()
plt.savefig('images/toutes_figures.png', dpi=150)
plt.close()
print("Image generee : images/toutes_figures.png")