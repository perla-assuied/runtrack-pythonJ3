class Personnage:
    def __init__(self, nom, vie):
        self.nom = nom  
        self.vie = vie  
    def attaquer(self, adversaire, degats):
        """La méthode attaquer permet d'infliger des dégâts à un adversaire."""
        adversaire.vie -= degats  
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} dégâts.")
    
    def est_vivant(self):
        """Vérifie si le personnage est toujours en vie (si ses points de vie > 0)."""
        return self.vie > 0
class Jeu:
    def __init__(self):
        self.niveau = None 
        self.joueur = None 
        self.ennemi = None  
    def choisir_niveau(self):
        """Demande au joueur de choisir un niveau de difficulté."""
        print("Choisissez un niveau de difficulté:")
        print("1. Facile")
        print("2. Moyen")
        print("3. Difficile")
        choix = int(input("Entrez le numéros du niveau choisi: "))
        if choix == 1:
            self.niveau = "Facile"
        elif choix == 2:
            self.niveau = "Moyen"
        elif choix == 3:
            self.niveau = "Difficile"
        else:
            print("Choix mauvaos, niveau facile par défaut.")
            self.niveau = "Facile"
