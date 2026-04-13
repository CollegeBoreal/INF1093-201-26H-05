import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def tracer_polygone(x, y, titre):
    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title(titre)
    plt.axis("equal")
    plt.grid(True)
    plt.show()


def afficher_carre(carre):
    cote = carre.cote
    x = [0, cote, cote, 0, 0]
    y = [0, 0, cote, cote, 0]
    tracer_polygone(x, y, f"Carré — côté={cote}, aire={carre.aire()}")


def afficher_cercle(cercle):
    r = cercle.rayon
    theta = np.linspace(0, 2 * np.pi, 300)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title(f"Cercle — rayon={r}, aire={cercle.aire():.2f}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


def afficher_triangle(triangle):
    base = triangle.base
    hauteur = triangle.hauteur
    x = [0, base, base / 2, 0]
    y = [0, 0, hauteur, 0]
    tracer_polygone(x, y, f"Triangle — base={base}, hauteur={hauteur}, aire={triangle.aire()}")


def afficher_rectangle(rectangle):
    x = [0, rectangle.longueur, rectangle.longueur, 0, 0]
    y = [0, 0, rectangle.largeur, rectangle.largeur, 0]
    tracer_polygone(x, y, f"Rectangle — longueur={rectangle.longueur}, largeur={rectangle.largeur}, aire={rectangle.aire()}")


def afficher_losange(losange):
    d1, d2 = losange.diagonale1, losange.diagonale2
    x = [0, d1 / 2, 0, -d1 / 2, 0]
    y = [d2 / 2, 0, -d2 / 2, 0, d2 / 2]
    tracer_polygone(x, y, f"Losange — d1={d1}, d2={d2}, aire={losange.aire()}")


def afficher_trapeze(trapeze):
    b1, b2, h = trapeze.base1, trapeze.base2, trapeze.hauteur
    decalage = (b1 - b2) / 2
    x = [0, b1, decalage + b2, decalage, 0]
    y = [0, 0, h, h, 0]
    tracer_polygone(x, y, f"Trapèze — bases={b1}/{b2}, hauteur={h}, aire={trapeze.aire()}")


def afficher_parallelogramme(parallelogramme):
    b, h, d = parallelogramme.base, parallelogramme.hauteur, parallelogramme.decalage
    x = [0, b, b + d, d, 0]
    y = [0, 0, h, h, 0]
    tracer_polygone(x, y, f"Parallélogramme — base={b}, hauteur={h}, aire={parallelogramme.aire()}")


def polygone_regulier(n, rayon):
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = rayon * np.cos(angles)
    y = rayon * np.sin(angles)
    x = np.append(x, x[0])
    y = np.append(y, y[0])
    return x, y


def afficher_pentagone(pentagone):
    x, y = polygone_regulier(5, pentagone.rayon)
    tracer_polygone(x, y, f"Pentagone — rayon={pentagone.rayon}, aire={pentagone.aire():.2f}")


def afficher_hexagone(hexagone):
    x, y = polygone_regulier(6, hexagone.rayon)
    tracer_polygone(x, y, f"Hexagone — rayon={hexagone.rayon}, aire={hexagone.aire():.2f}")


def afficher_octogone(octogone):
    x, y = polygone_regulier(8, octogone.rayon)
    tracer_polygone(x, y, f"Octogone — rayon={octogone.rayon}, aire={octogone.aire():.2f}")


def afficher_ellipse(ellipse):
    t = np.linspace(0, 2 * np.pi, 400)
    x = ellipse.a * np.cos(t)
    y = ellipse.b * np.sin(t)
    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title(f"Ellipse — a={ellipse.a}, b={ellipse.b}, aire={ellipse.aire():.2f}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


def afficher_etoile(etoile):
    angles = np.linspace(0, 2 * np.pi, etoile.branches * 2, endpoint=False)
    rayons = np.array([
        etoile.rayon_externe if i % 2 == 0 else etoile.rayon_interne
        for i in range(etoile.branches * 2)
    ])
    x = rayons * np.cos(angles + np.pi / 2)
    y = rayons * np.sin(angles + np.pi / 2)
    x = np.append(x, x[0])
    y = np.append(y, y[0])
    plt.figure(figsize=(5, 5))
    plt.plot(x, y)
    plt.fill(x, y, alpha=0.3)
    plt.title(f"Étoile — branches={etoile.branches}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


def afficher_cube_3d(cube):
    cote = cube.cote
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    sommets = np.array([
        [0, 0, 0], [cote, 0, 0], [cote, cote, 0], [0, cote, 0],
        [0, 0, cote], [cote, 0, cote], [cote, cote, cote], [0, cote, cote]
    ])
    faces = [
        [sommets[j] for j in [0, 1, 2, 3]],
        [sommets[j] for j in [4, 5, 6, 7]],
        [sommets[j] for j in [0, 1, 5, 4]],
        [sommets[j] for j in [2, 3, 7, 6]],
        [sommets[j] for j in [1, 2, 6, 5]],
        [sommets[j] for j in [4, 7, 3, 0]],
    ]
    ax.add_collection3d(Poly3DCollection(faces, alpha=0.25, edgecolor='black'))
    ax.scatter(sommets[:, 0], sommets[:, 1], sommets[:, 2])
    ax.set_xlim(0, cote)
    ax.set_ylim(0, cote)
    ax.set_zlim(0, cote)
    ax.set_title(f"Cube 3D — côté={cote}, volume={cube.volume()}")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()
