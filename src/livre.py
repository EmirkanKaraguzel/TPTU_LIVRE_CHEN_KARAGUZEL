from src.auteur import Auteur  

class Livre:
    def __init__(self, titre: str, pages: int, auteur: Auteur = None):
        self._titre = titre
        self._pages = pages
        self._auteur = None  
        if auteur:
            self.set_auteur(auteur)

    def get_titre(self) -> str:
        return self._titre

    def get_pages(self) -> int:
        return self._pages

    def get_auteur(self) -> Auteur:
        return self._auteur

    def set_auteur(self, auteur: Auteur):
        """Associe ou dissocie un auteur au livre de manière sécurisée."""
        if self._auteur == auteur:
            return

        # ✅ Suppression de l'ancien auteur s'il existe
        if self._auteur is not None:
            if self in self._auteur.get_livres():
                self._auteur._livres.remove(self)

        # ✅ Mise à jour du nouvel auteur
        self._auteur = auteur

        if auteur is not None:
            auteur.ajouter_livre(self)



    def modifier_livre(self, nouveau_titre: str, ajout_pages: int):
        self._titre = nouveau_titre
        if ajout_pages > 0:
            self._pages += ajout_pages

    def get_biographie_auteur(self) -> str:  # ✅ Extract Method
        """Retourne la biographie de l’auteur ou 'Auteur inconnu'."""
        return self._auteur.biographie() if self._auteur else "Auteur inconnu."

    def afficher_details(self) -> str:
        """Affiche les détails du livre."""
        details = f"Livre : {self._titre} ({self._pages} pages)"
        details += f"\n{self.get_biographie_auteur()}"
        return details
