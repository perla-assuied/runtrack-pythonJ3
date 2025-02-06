# J'ai décidé de créer une classe Ville et une classe Personne. La classe Ville a un attribut privé __habitants qui représente le nombre d'habitants de la ville. La classe Ville a une méthode augmenter_population qui permet d'ajouter 1 au nombre d'habitants. La classe Personne a un attribut privé __ville qui représente la ville où habite la personne. La classe Personne a une méthode ajouter_population qui permet d'ajouter 1 à la population de la ville où habite la personne. J'ai créé deux objets Ville, Paris et Marseille, avec un nombre d'habitants initial. J'ai créé trois objets Personne, John, Myrtille et Chloé, qui habitent respectivement à Paris, Paris et Marseille. J'ai ajouté les nouvelles personnes à leur ville respective et j'ai affiché le nombre d'habitants avant et après l'ajout des nouvelles personnes.
class Ville:
    def __init__(self, nom, habitants):
        self.__nom = nom
        self.__habitants = habitants

    # C'est la méthode pour obtenir le nombre d'habitants
    def get_habitants(self):
        return self.__habitants

    # C'est la méthode pour augmenter la population de la ville
    def augmenter_population(self):
        self.__habitants += 1

class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    # C'est la méthode pour ajouter une personne à la population de la ville
    def ajouter_population(self):
        self.__ville.augmenter_population()

# Je crée des objet ville Paris et Marseille
paris = Ville("Paris", 1000000)
marseille = Ville("Marseille", 861635)

# J'affiche le nombre d'habitants avant l'ajout des nouvelles personnes
print(f"Nombre d'habitants de Paris avant l'arrivée: {paris.get_habitants()}")
print(f"Nombre d'habitants de Marseille avant l'arrivée: {marseille.get_habitants()}")

# Je crée des objets personne John, Myrtille et Chloé
john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

# J'ajoute les nouvelles personnes à leur ville respective
john.ajouter_population()
myrtille.ajouter_population()
chloe.ajouter_population()

# J'affiche le nombre d'habitants apres l'ajout des nouvelles personnes  
print(f"Nombre d'habitants de Paris après l'arrivée: {paris.get_habitants()}")
print(f"Nombre d'habitants de Marseille après l'arrivée: {marseille.get_habitants()}")