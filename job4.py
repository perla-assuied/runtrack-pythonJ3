# J'ai d'abord crée la classe Joueur, j'ai initialisé leurs nom, leur position, leurs buts, leurs passes décisives, leurs cartons jaunes et leurs cartons rouges. J'ai crée la classe Equipe, j'ai initialisé le nom de l'équipe et une liste vide pour stocker les joueurs. La classe Equipe a une méthode pour ajouter un joueur à l'équipe et une méthode pour afficher les statistiques de tous les joueurs de l'équipe. J'ai crée des joueurs Lionel Messi, Cristiano Ronaldo, Andres Iniesta et Sergio Ramos. J'ai crée des équipes Barça et Real Madrid. J'ai ajouté les joueurs aux équipes. J'ai affiché les statistiques initiales des joueurs. J'ai simulé un match avec des actions de joueurs. J'ai mis à jour les statistiques des joueurs dans l'équipe. J'ai affiché les statistiques finales après le match. J'ai crée une classe Joueur, j'ai initialisé leurs nom, leur position, leurs buts, leurs passes décisives, leurs cartons jaunes et leurs cartons rouges. J'ai crée la classe Equipe, j'ai initialisé le nom de l'équipe et une liste vide pour stocker les joueurs. La classe Equipe a une méthode pour ajouter un joueur à l'équipe et une méthode pour afficher les statistiques de tous les joueurs de l'équipe. J'ai crée des joueurs Lionel Messi, Cristiano Ronaldo, Andres Iniesta et Sergio Ramos. J'ai crée des équipes Barça et Real Madrid. J'ai ajouté les joueurs aux équipes. J'ai affiché les statistiques initiales des joueurs. J'ai simulé un match avec des actions de joueurs. J'ai mis à jour les statistiques des joueurs dans l'équipe. J'ai affiché les statistiques finales après le match. J'ai crée une classe Joueur, j'ai initialisé leurs nom, leur position, leurs buts, leurs passes décisives, leurs cartons jaunes et leurs cartons rouges. J'ai crée la classe Equipe, j'ai initialisé le nom de l'équipe et une liste vide pour stocker les joueurs. La classe Equipe a une méthode pour ajouter un joueur à l'équipe et une méthode pour afficher les statistiques de tous les joueurs de l'équipe. J'ai crée des joueurs Lionel Messi, Cristiano Ronaldo, Andres Iniesta et Sergio Ramos. J'ai crée des équipes Barça et Real Madrid. J'ai ajouté les joueurs aux équipes. J'ai affiché les statistiques initiales des joueurs. J'ai simulé un match avec des actions de joueurs. J'ai mis à jour les statistiques des joueurs dans l'équipe. J'ai affiché les statistiques finales après le match. J'ai crée une classe Joueur, j'ai initialisé leurs nom, leur position, leurs buts, leurs passes décisives, leurs cartons jaunes et leurs cartons rouges. J'ai crée la classe Equipe, j'ai initialisé le nom de l'équipe et une liste vide pour stocker les joueurs. La classe Equipe a une méthode pour ajouter un joueur à l'équipe et une méthode pour afficher les statistiques de tous les joueurs de l'équipe. J'ai crée des joueurs Lionel Messi, Cristiano Ronaldo, Andres Iniesta et Sergio Ramos. J'ai crée des équipes Barça et Real Madrid. J'ai ajouté les joueurs aux équipes. J'ai affiché les statistiques initiales des joueurs. J'ai simulé un match avec des actions de joueurs. J'ai mis à jour les statistiques des joueurs dans l'équipe. J'ai affiché les statistiques finales après le match.
class Joueur:
    def __init__(self, nom, numero, position):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.buts = 0
        self.passes_decisives = 0
        self.cartons_jaunes = 0
        self.cartons_rouges = 0

    def marquerUnBut(self):
        """Le joueur marque un but."""
        self.buts += 1
        print(f"{self.nom} a marqué un but !")

    def effectuerUnePasseDecisive(self):
        """Le joueur effectue une passe décisive."""
        self.passes_decisives += 1
        print(f"{self.nom} a effectué une passe décisive !")

    def recevoirUnCartonJaune(self):
        """Le joueur reçoit un carton jaune."""
        self.cartons_jaunes += 1
        print(f"{self.nom} a reçu un carton jaune !")

    def recevoirUnCartonRouge(self):
        """Le joueur reçoit un carton rouge."""
        self.cartons_rouges += 1
        print(f"{self.nom} a reçu un carton rouge !")

    def afficherStatistiques(self):
        """Affiche les statistiques du joueur."""
        print(f"Statistiques de {self.nom}:")
        print(f"Numéro: {self.numero}")
        print(f"Position: {self.position}")
        print(f"Buts marqués: {self.buts}")
        print(f"Passes décisives: {self.passes_decisives}")
        print(f"Cartons jaunes reçus: {self.cartons_jaunes}")
        print(f"Cartons rouges reçus: {self.cartons_rouges}")
        print("-" * 30)
class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []  

    def ajouterJoueur(self, joueur):
        """Ajoute un joueur à l'équipe."""
        self.joueurs.append(joueur)
        print(f"{joueur.nom} a été ajouté à l'équipe {self.nom}.")

    def afficherStatistiquesJoueurs(self):
        """Affiche les statistiques de tous les joueurs de l'équipe."""
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, action):
        """Met à jour les statistiques d'un joueur en fonction de l'action."""
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                action(joueur)
                return
        print(f"Le joueur {nom_joueur} n'est pas dans l'équipe.")
        
joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
joueur2 = Joueur("Cristiano Ronaldo", 7, "Attaquant")
joueur3 = Joueur("Andres Iniesta", 8, "Milieu")
joueur4 = Joueur("Sergio Ramos", 4, "Défenseur")

equipe1 = Equipe("Barça")
equipe2 = Equipe("Real Madrid")

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur3)

equipe2.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur4)

equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()

print("\nMatch en cours...")
joueur1.marquerUnBut()
joueur2.marquerUnBut()
joueur3.effectuerUnePasseDecisive()
joueur4.recevoirUnCartonJaune()
joueur1.marquerUnBut()
joueur2.recevoirUnCartonRouge()
equipe1.mettreAJourStatistiquesJoueur("Lionel Messi", Joueur.marquerUnBut)
equipe2.mettreAJourStatistiquesJoueur("Cristiano Ronaldo", Joueur.recevoirUnCartonRouge)

print("\nStatistiques finales après le match:")
equipe1.afficherStatistiquesJoueurs()
equipe2.afficherStatistiquesJoueurs()