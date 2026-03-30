import matplotlib.pyplot as plt
import numpy as np

def afficher_carre(carre):
    cote = carre.cote
    x = [0, cote, cote, 0, 0]
    y = [0, 0, cote, cote, 0]

    plt.figure(figsize=(5,5))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title(f"Carré — côté={cote}, aire={carre.aire()}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

def afficher_cercle(cercle):
    r = cercle.rayon
    theta = np.linspace(0, 2*np.pi, 300)
    x = r * np.cos(theta)
    y = r * np.sin(theta)

    plt.figure(figsize=(5,5))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title(f"Cercle — rayon={r}, aire={cercle.aire():.2f}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

def afficher_triangle(triangle):
    x = [0, triangle.base, 0, 0]
    y = [0, 0, triangle.hauteur, 0]

    plt.figure(figsize=(5,5))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title(f"Triangle — base={triangle.base}, hauteur={triangle.hauteur}, aire={triangle.aire()}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()