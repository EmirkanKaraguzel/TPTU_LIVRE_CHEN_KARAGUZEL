import unittest
from src.livre import Livre
from src.auteur import Auteur

class TestRelationAuteurLivre(unittest.TestCase):

    def setUp(self):
        """Fixture : Création d’auteurs et de livres pour tester la relation"""
        self.auteur1 = Auteur("J.K. Rowling")
        self.auteur2 = Auteur("Victor Hugo")

        self.livre1 = Livre("Harry Potter", 300, self.auteur1)
        self.livre2 = Livre("Harry Potter 2", 350, self.auteur1)
        self.livre3 = Livre("Les Misérables", 1200, self.auteur2)

    def test_auteur_peut_avoir_plusieurs_livres(self):
        """Vérifie qu’un auteur peut écrire plusieurs livres"""
        self.assertEqual(len(self.auteur1.get_livres()), 2)
        self.assertEqual(self.auteur1.get_livres()[0].get_titre(), "Harry Potter")

    def test_reassigner_auteur(self):
        """Vérifie qu’un livre peut changer d’auteur et que les listes sont mises à jour"""
        self.livre1.set_auteur(self.auteur2)  # On change l'auteur de Harry Potter
        self.assertEqual(self.livre1.get_auteur().get_nom_auteur(), "Victor Hugo")
        self.assertIn(self.livre1, self.auteur2.get_livres())  # Victor Hugo a récupéré le livre
        self.assertNotIn(self.livre1, self.auteur1.get_livres())  # J.K. Rowling l’a perdu

    def test_afficher_details(self):
        """Vérifie l'affichage des détails du livre avec la nouvelle biographie"""
        details_attendus = "Livre : Harry Potter (300 pages)\nAuteur : J.K. Rowling - Œuvres : Harry Potter, Harry Potter 2."
        self.assertEqual(self.livre1.afficher_details(), details_attendus)

    def test_supprimer_livre(self):
        """Vérifie que la suppression d'un livre fonctionne correctement"""
        self.auteur1.supprimer_livre(self.livre1)
        self.assertNotIn(self.livre1, self.auteur1.get_livres())

if __name__ == '__main__':
    unittest.main()
