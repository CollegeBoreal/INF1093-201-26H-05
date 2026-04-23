import math


class Tore:
    def __init__(self, grand_rayon, petit_rayon):
        self.grand_rayon = grand_rayon
        self.petit_rayon = petit_rayon

    def aire(self):
        return 4 * math.pi ** 2 * self.grand_rayon * self.petit_rayon

    def volume(self):
        return 2 * math.pi ** 2 * self.grand_rayon * self.petit_rayon ** 2

    def afficher_info(self):
        return f"Tore de grand rayon {self.grand_rayon} et petit rayon {self.petit_rayon}"
