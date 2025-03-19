Feature: Gestion des livres et auteurs

  Scenario: Un auteur peut avoir plusieurs livres
    Given un auteur "J.K. Rowling"
    And il n'a aucun livre enregistré
    When j'ajoute les livres "Harry Potter" et "Harry Potter 2" à cet auteur
    Then la liste des œuvres de "J.K. Rowling" doit contenir "Harry Potter" et "Harry Potter 2"

  Scenario: Un livre a toujours un seul auteur
    Given un livre "Harry Potter" attribué à "J.K. Rowling"
    When je change son auteur pour "Stephen King"
    Then "J.K. Rowling" ne doit plus être listé comme auteur du livre
    And "Stephen King" doit être le nouvel auteur du livre

  Scenario: Affichage des détails d’un livre
    Given un livre "Harry Potter" avec 300 pages écrit par "J.K. Rowling"
    When je consulte ses détails
    Then l'affichage doit inclure "Harry Potter", "300", et "J.K. Rowling"

  Scenario: Modifier les informations d’un livre
    Given un livre "Harry Potter" avec 300 pages
    When je modifie son titre en "Harry Potter et la Chambre des Secrets" et j’ajoute 50 pages
    Then le titre doit être "Harry Potter et la Chambre des Secrets"
    And le nombre total de pages doit être "350"

  Scenario: Suppression d’un livre
    Given un auteur "J.K. Rowling" ayant le livre "Harry Potter"
    When je supprime "Harry Potter"
    Then "Harry Potter" ne doit plus apparaître dans la liste des livres de "J.K. Rowling"
