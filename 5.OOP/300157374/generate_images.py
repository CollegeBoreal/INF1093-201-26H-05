import matplotlib.pyplot as plt
import numpy as np

# --- Carre ---
cote = 4
x = [0, cote, cote, 0, 0]
y = [0, 0, cote, cote, 0]
plt.figure(figsize=(5, 5))
plt.plot(x, y, 'b-')
plt.fill(x, y, alpha=0.3, color='blue')
plt.title(f'Carre - cote={cote}, aire={cote**2}')
plt.axis('equal')
plt.grid(True)
plt.savefig('images/carre.png')
plt.close()

# --- Cercle ---
r = 3
theta = np.linspace(0, 2*np.pi, 300)
x = r * np.cos(theta)
y = r * np.sin(theta)
plt.figure(figsize=(5, 5))
plt.plot(x, y, 'r-')
plt.fill(x, y, alpha=0.3, color='red')
plt.title(f'Cercle - rayon={r}, aire={3.14159*r**2:.2f}')
plt.axis('equal')
plt.grid(True)
plt.savefig('images/cercle.png')
plt.close()

# --- Triangle ---
b, h = 5, 2
x = [0, b, b/2, 0]
y = [0, 0, h, 0]
plt.figure(figsize=(5, 5))
plt.plot(x, y, 'g-')
plt.fill(x, y, alpha=0.3, color='green')
plt.title(f'Triangle - base={b}, hauteur={h}, aire={b*h/2}')
plt.axis('equal')
plt.grid(True)
plt.savefig('images/triangle.png')
plt.close()

print("Images generees dans images/")
