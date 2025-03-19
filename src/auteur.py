class Auteur:
    def __init__(self, nom: str):
        self._nom = nom
        self._livres = []  # Liste des livres écrits par cet auteur

    def get_nom_auteur(self) -> str:  # Rename : get_nom → get_nom_auteur
        return self._nom

    def changer_nom_auteur(self, nom: str):  #  Rename : set_nom → changer_nom_auteur
        self._nom = nom

    def ajouter_livre(self, livre):
        """Ajoute un livre à l’auteur si ce n’est pas déjà fait."""
        if livre not in self._livres:
            self._livres.append(livre)
            if livre.get_auteur() != self:
                livre.set_auteur(self)  

    def get_livres(self):
        """Retourne tous les livres écrits par cet auteur."""
        return list(self._livres)  # Retourne une copie pour éviter la modification externe

    def biographie(self) -> str:
        if self._livres:
            livres_str = ", ".join([livre.get_titre() for livre in self._livres])
            return f"Auteur : {self._nom} - Œuvres : {livres_str}."
        return f"Auteur : {self._nom} - Aucun livre enregistré."
        
    def supprimer_livre(self, livre):
        """Supprime un livre de la liste des livres de l'auteur et met à jour la relation bidirectionnelle"""
        if livre in self._livres:
            self._livres.remove(livre)
            livre.set_auteur(None)
