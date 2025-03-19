from behave import given, when, then
from src.livre import Livre
from src.auteur import Auteur

# Stocke les objets créés pendant les tests
contexte_auteurs = {}
contexte_livres = {}

@given('un auteur "{nom}"')
def step_creer_auteur(context, nom):
    contexte_auteurs[nom] = Auteur(nom)

@given('il n\'a aucun livre enregistré')
def step_verifier_auteur_sans_livre(context):
    for auteur in contexte_auteurs.values():
        assert len(auteur.get_livres()) == 0

@when('j\'ajoute les livres "{livre1}" et "{livre2}" à cet auteur')
def step_ajouter_livres_auteur(context, livre1, livre2):
    auteur = list(contexte_auteurs.values())[0]
    contexte_livres[livre1] = Livre(livre1, 300, auteur)
    contexte_livres[livre2] = Livre(livre2, 350, auteur)

@then('la liste des œuvres de "{nom}" doit contenir "{livre1}" et "{livre2}"')
def step_verifier_liste_livres(context, nom, livre1, livre2):
    auteur = contexte_auteurs[nom]
    livres = [livre.get_titre() for livre in auteur.get_livres()]
    assert livre1 in livres and livre2 in livres

@given('un livre "{titre}" attribué à "{nom}"')
def step_creer_livre(context, titre, nom):
    contexte_livres[titre] = Livre(titre, 300, contexte_auteurs[nom])

@when('je change son auteur pour "{nouvelAuteur}"')
def step_modifier_auteur(context, nouvelAuteur):
    livre = list(contexte_livres.values())[0]
    contexte_auteurs[nouvelAuteur] = Auteur(nouvelAuteur)
    livre.set_auteur(contexte_auteurs[nouvelAuteur])

@then('"{ancienAuteur}" ne doit plus être listé comme auteur du livre')
def step_verifier_ancien_auteur(context, ancienAuteur):
    livre = list(contexte_livres.values())[0]
    assert livre.get_auteur().get_nom_auteur() != ancienAuteur

@then('"{nouvelAuteur}" doit être le nouvel auteur du livre')
def step_verifier_nouvel_auteur(context, nouvelAuteur):
    livre = list(contexte_livres.values())[0]
    assert livre.get_auteur().get_nom_auteur() == nouvelAuteur

@when('je consulte ses détails')
def step_afficher_details(context):
    context.details = list(contexte_livres.values())[0].afficher_details()

@then('l\'affichage doit inclure "{titre}", "{pages}", et "{auteur}"')
def step_verifier_affichage(context, titre, pages, auteur):
    assert titre in context.details
    assert pages in context.details
    assert auteur in context.details

@when('je modifie son titre en "{nouveauTitre}" et j\'ajoute {ajoutPages:d} pages')
def step_modifier_livre(context, nouveauTitre, ajoutPages):
    livre = list(contexte_livres.values())[0]
    livre.modifier_livre(nouveauTitre, ajoutPages)



@when('je supprime "{livre}"')
def step_supprimer_livre(context, livre):
    """Supprime un livre et s’assure qu'il est bien dissocié de l’auteur."""
    contexte_livre_obj = contexte_livres[livre]  # Récupère la bonne instance du livre
    auteur = contexte_livre_obj.get_auteur()  # Utilise l’auteur réel du livre

    if auteur is not None:  #Vérifie que l’auteur n’est pas déjà None
        auteur.supprimer_livre(contexte_livre_obj)  # Supprime le livre via l’auteur correct


@then('"{livre}" ne doit plus apparaître dans la liste des livres de "{auteur}"')
def step_verifier_suppression_livre(context, livre, auteur):
    """Vérifie que le livre a bien été supprimé de la liste des œuvres de l’auteur."""
    auteur_obj = contexte_livres[livre].get_auteur()  # On récupère l’auteur via l’objet livre mis à jour
    if auteur_obj:
        livres_de_auteur = [l.get_titre() for l in auteur_obj.get_livres()]
    else:
        livres_de_auteur = []
    assert livre not in livres_de_auteur, f" Erreur: {livre} est toujours dans la liste de {auteur} !"



@given('un livre "{titre}" avec {pages:d} pages écrit par "{auteur}"')
def step_creer_livre_avec_auteur(context, titre, pages, auteur):
    """Crée un livre avec un nombre de pages et un auteur."""
    contexte_auteurs[auteur] = Auteur(auteur)
    contexte_livres[titre] = Livre(titre, pages, contexte_auteurs[auteur])

@given('un livre "{titre}" avec {pages:d} pages')
def step_creer_livre_sans_auteur(context, titre, pages):
    """Crée un livre avec un nombre de pages mais sans auteur."""
    contexte_livres[titre] = Livre(titre, pages)

@when('je modifie son titre en "{nouveauTitre}" et j’ajoute {ajoutPages:d} pages')
def step_modifier_livre(context, nouveauTitre, ajoutPages):
    """Modifie le titre et le nombre de pages d’un livre."""
    livre = list(contexte_livres.values())[0]
    livre.modifier_livre(nouveauTitre, ajoutPages)

@then('le titre doit être "{nouveauTitre}"')
def step_verifier_titre(context, nouveauTitre):
    """Vérifie que le titre du livre a bien été modifié."""
    livre = list(contexte_livres.values())[0]
    assert livre.get_titre() == nouveauTitre

@then('le nombre total de pages doit être "{pagesFinal}"')
def step_verifier_nombre_pages(context, pagesFinal):
    """Vérifie que le nombre de pages du livre a bien été mis à jour."""
    livre = list(contexte_livres.values())[0]
    assert str(livre.get_pages()) == pagesFinal
