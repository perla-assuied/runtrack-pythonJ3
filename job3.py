# J'ai dabord créé une classe tache, avec le titre de la tache, sa description et son statut. J'ai ensuite créé une classe ListeDeTaches, qui contient une liste de taches. La classe ListeDeTaches a des méthodes pour ajouter une tache à la liste, supprimer une tache de la liste, marquer une tache comme terminée, afficher toutes les taches et filtrer les taches par statut. J'ai créé une liste de taches et ajouté quelques taches à la liste. J'ai affiché la liste des taches, marqué une tache comme terminée, affiché la liste mise à jour, supprimé une tache de la liste, affiché la liste après suppression, filtré les taches à faire et les taches terminées, et affiché les taches filtrées. Ensuite, j'ai créé une liste de taches, ajouté quelques taches à la liste, affiché la liste des taches, marqué une tache comme terminée, affiché la liste mise à jour, supprimé une tache de la liste, affiché la liste après suppression, filtré les taches à faire et les taches terminées, et affiché les taches filtrées. Puis j'ai créé une liste de taches, ajouté quelques taches à la liste, affiché la liste des taches, marqué une tache comme terminée, affiché la liste mise à jour, supprimé une tache de la liste, affiché la liste après suppression, filtré les taches à faire et les taches terminées, et affiché les taches filtrées. Enfin, j'ai créé une liste de taches, ajouté quelques taches à la liste, affiché la liste des taches, marqué une tache comme terminée, affiché la liste mise à jour, supprimé une tache de la liste, affiché la liste après suppression, filtré les taches à faire et les taches terminées, et affiché les taches filtrées.
class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre         
        self.description = description  
        self.statut = statut      
    
    def marquerCommeFinie(self):
        """Marque la tâche comme terminée."""
        self.statut = "terminée"
        print(f"Tâche '{self.titre}' marquée comme terminée.")
    
    def __str__(self):
        """Retourne une représentation en chaîne de caractères de la tâche."""
        return f"{self.titre} - {self.statut}: {self.description}"
class ListeDeTaches:
    def __init__(self):
        self.taches = []  

    def ajouterTache(self, tache):
        """Ajoute une tâche à la liste."""
        self.taches.append(tache)
        print(f"Tâche '{tache.titre}' ajoutée à la liste.")
    
    def supprimerTache(self, titre):
        """Supprime une tâche de la liste par son titre."""
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                print(f"Tâche '{titre}' supprimée de la liste.")
                return
        print(f"Aucune tâche trouvée avec le titre '{titre}'.")
    
    def marquerCommeFinie(self, titre):
        """Marque une tâche comme terminée par son titre."""
        for tache in self.taches:
            if tache.titre == titre:
                tache.marquerCommeFinie()
                return
        print(f"Aucune tâche trouvée avec le titre '{titre}'.")
    
    def afficherListe(self):
        """Affiche toutes les tâches."""
        if not self.taches:
            print("Aucune tâche à afficher.")
        else:
            for tache in self.taches:
                print(tache)
    
    def filterListe(self, statut):
        """Filtre les tâches par statut et retourne cette liste."""
        taches_filtrees = [tache for tache in self.taches if tache.statut == statut]
        return taches_filtrees
liste_de_taches = ListeDeTaches()

tache1 = Tache("Faire les courses", "Acheter des fruits et légumes")
tache2 = Tache("Répondre aux emails", "Répondre à tous les emails en retard")
tache3 = Tache("Préparer le dîner", "Préparer un repas pour la famille")
tache4 = Tache("Nettoyer la maison", "Faire le ménage dans toute la maison")

liste_de_taches.ajouterTache(tache1)
liste_de_taches.ajouterTache(tache2)
liste_de_taches.ajouterTache(tache3)
liste_de_taches.ajouterTache(tache4)

print("\nListe des tâches:")
liste_de_taches.afficherListe()

liste_de_taches.marquerCommeFinie("Faire les courses")

print("\nListe des tâches après modification:")
liste_de_taches.afficherListe()

liste_de_taches.supprimerTache("Nettoyer la maison")

print("\nListe des tâches après suppression:")
liste_de_taches.afficherListe()

taches_a_faire = liste_de_taches.filterListe("à faire")
print("\nTâches à faire:")
for tache in taches_a_faire:
    print(tache)

taches_terminees = liste_de_taches.filterListe("terminée")
print("\nTâches terminées:")
for tache in taches_terminees:
    print(tache)