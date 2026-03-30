from Carre import Carre
from Cercle import Cercle
from Triangle import Triangle
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
    plt.figure(figsize=(5,5))
    x = [0, triangle.base, triangle.base, 0]
    y = [0, 0, triangle.hauteur, 0]
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title(f"Triangle — base={triangle.base}, hauteur={triangle.hauteur}, aire={triangle.aire()}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

def main():
    formes = [Carre(4), Cercle(3), Triangle(5, 2)]
    for f in formes:
        print(f.afficher_info())
        if isinstance(f, Carre):
            afficher_carre(f)
        elif isinstance(f, Cercle):
            afficher_cercle(f)
        elif isinstance(f, Triangle):
            afficher_triangle(f)

if __name__ == "__main__":
    main()