
import math


class Hemisphere:
    def __init__(self, rayon):
        self.rayon = rayon

    def aire(self):
        return 3 * math.pi * self.rayon ** 2

    def volume(self):
        return (2 / 3) * math.pi * self.rayon ** 3

    def afficher_info(self):
        return f"Hémisphère de rayon {self.rayon}"
