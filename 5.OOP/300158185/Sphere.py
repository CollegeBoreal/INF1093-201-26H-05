import math


class Sphere:
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return 4 * math.pi * self.rayon ** 2

    def volume(self):
        return (4 / 3) * math.pi * self.rayon ** 3

    def afficher_info(self):
        return f"Sphère de rayon {self.rayon}"
