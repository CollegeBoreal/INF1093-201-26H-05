from Figure import Figure

class Etoile(Figure):
    def __init__(self, rayon_externe: float, rayon_interne: float, branches: int = 5):
        self.rayon_externe = rayon_externe
        self.rayon_interne = rayon_interne
        self.branches = branches

    def aire(self):
        return "Aire approximative non définie dans ce projet"

    def afficher_info(self):
        return f"Étoile de {self.branches} branches"
