import math

class Figure:
    def aire(self):
        raise NotImplementedError("La méthode aire() doit être redéfinie.")

    def afficher_info(self):
        return f"Figure : {self.__class__.__name__}"
