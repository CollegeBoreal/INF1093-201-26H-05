from Carre import Carre
from Rectangle import Rectangle
from Triangle import Triangle
from Cercle import Cercle
from Losange import Losange
from Trapeze import Trapeze
from Parallelogramme import Parallelogramme
from Pentagone import Pentagone
from Hexagone import Hexagone
from Octogone import Octogone
from Ovale import Ovale
from Anneau import Anneau

from Cube import Cube
from Sphere import Sphere
from Cylindre import Cylindre
from Cone import Cone
from Pyramide import Pyramide
from Prisme import Prisme
from Tore import Tore
from Hemisphere import Hemisphere


def afficher_infos(forme):
    print("=" * 50)
    print(f"Forme : {forme.__class__.__name__}")

    if hasattr(forme, "afficher_infos"):
        try:
            forme.afficher_infos()
        except:
            pass

    if hasattr(forme, "aire"):
        try:
            print("Aire :", forme.aire())
        except:
            pass

    if hasattr(forme, "surface"):
        try:
            print("Surface :", forme.surface())
        except:
            pass

    if hasattr(forme, "volume"):
        try:
            print("Volume :", forme.volume())
        except:
            pass


def main():
    formes = [
        Carre(4),
        Rectangle(6, 3),
        Triangle(5, 4),
        Cercle(3),
        Losange(6, 4),
        Trapeze(7, 5, 4),
        Parallelogramme(6, 3),
        Pentagone(4, 2.75),
        Hexagone(4, 3.46),
        Octogone(4, 4.83),
        Ovale(5, 3),
        Anneau(5, 2),

        Cube(3),
        Sphere(3),
        Cylindre(3, 5),
        Cone(3, 5),
        Pyramide(4, 6),
        Prisme(4, 6),
        Tore(5, 2),
        Hemisphere(3)
    ]

    print("\nAFFICHAGE DES 20 FORMES\n")

    for forme in formes:
        afficher_infos(forme)


if __name__ == "__main__":
    main()
