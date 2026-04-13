class Parallelogramme:
    def __init__(self, base, hauteur):
        self.base = base
        self.hauteur = hauteur

    def aire(self):
        return self.base * self.hauteur

    def afficher_info(self):
        return f"Parallélogramme de base {self.base} et hauteur {self.hauteur}"
