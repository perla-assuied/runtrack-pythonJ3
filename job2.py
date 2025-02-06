# J'ai initialisé la classe CompteBancaire avec les attributs privés __numero_compte, __nom, __prenom, __solde et __decouvert. La classe CompteBancaire a une méthode afficher qui affiche les informations du compte, une méthode afficherSolde qui affiche le solde du compte, une méthode versement qui permet d'effectuer un versement, une méthode retrait qui permet d'effectuer un retrait, une méthode agios qui applique des agios si le solde est négatif et une méthode virement qui permet d'effectuer un virement vers un autre compte. J'ai créé deux objets CompteBancaire, compte1 et compte2, avec des soldes initiaux différents. J'ai effectué des opérations de versement, de retrait, d'application d'agios et de virement entre les deux comptes. J'ai affiché les informations des comptes après chaque opération, pour vérifier que les opérations ont été effectuées correctement.
class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte  
        self.__nom = nom  
        self.__prenom = prenom  
        self.__solde = solde  
        self.__decouvert = decouvert 

    # C'est la méthode pour afficher les informations du compte
    def afficher(self):
        print(f"Compte n°{self.__numero_compte}")
        print(f"Titulaire: {self.__prenom} {self.__nom}")
        print(f"Solde: {self.__solde}€")
        print(f"Droit au découvert: {'Oui' if self.__decouvert else 'Non'}")

    # C'est la méthode pour afficher le solde du compte
    def afficherSolde(self):
        print(f"Solde du compte: {self.__solde}€")

    # C'est la méthode pour effectuer un versement
    def versement(self, montant):
        if montant > 0:
            self.__solde += montant
            print(f"Versement de {montant}€ effectué. Nouveau solde: {self.__solde}€")
        else:
            print("Le montant du versement doit être positif.")

    # C'est la méthode pour effectuer un retrait
    def retrait(self, montant):
        if montant > self.__solde and not self.__decouvert:
            print("Erreur: Solde insuffisant et découvert non autorisé.")
        elif montant > 0:
            self.__solde -= montant
            print(f"Retrait de {montant}€ effectué. Nouveau solde: {self.__solde}€")
        else:
            print("Le montant du retrait doit être positif.")

    # C'est la méthode pour appliquer des agios si le solde est négatif
    def agios(self):
        if self.__solde < 0:
            agios = abs(self.__solde) * 0.05  # Exemple d'agios à 5% du montant négatif
            self.__solde -= agios
            print(f"Agios de {agios}€ appliqués. Nouveau solde: {self.__solde}€")

    # C'est la méthode pour effectuer un virement vers un autre compte
    def virement(self, compte_dest, montant):
        if montant > 0 and self.__solde >= montant:
            self.__solde -= montant
            compte_dest.versement(montant)
            print(f"Virement de {montant}€ effectué vers le compte n°{compte_dest.__numero_compte}.")
        else:
            print("Erreur: Solde insuffisant pour effectuer le virement.")
    # Je crée les taux des deux comptes bancaire
        compte1 = CompteBancaire("12345", "Dupont", "Jean", 1000)
        compte2 = CompteBancaire("67890", "Durand", "Marie", -200, decouvert=True)

    # J'affiche les informations des comptes
        compte1.afficher()
        compte2.afficher()

    # Versement sur le compte1
        compte1.versement(500)

    # Retrait du compte1
        compte1.retrait(300)

    # Retrait du compte2 (à découvert)
        compte2.retrait(50)

    # Application des agios sur le compte2 (solde négatif)
        compte2.agios()

    # Virement de compte1 vers compte2
        compte1.virement(compte2, 400)

    # Affichage des comptes après virement
        compte1.afficher()
        compte2.afficher()