
class Trapeze:
    def __init__(self, grande_base, petite_base, hauteur):
        self.grande_base = grande_base
        self.petite_base = petite_base
        self.hauteur = hauteur

    def aire(self):
        return ((self.grande_base + self.petite_base) * self.hauteur) / 2

    def afficher_info(self):
        return f"Trapèze de bases {self.grande_base} et {self.petite_base}, hauteur {self.hauteur}"
