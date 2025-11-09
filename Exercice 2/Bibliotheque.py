from document import Document
from livre import Livre
from magazine import Magazine

class Bibliotheque :
    def __init__(self,nom):
        self.__nom = nom
        self.docs = []

    def ajouter_docs(self, doc) :
        self.docs.append(doc)

    def afficher_docs(self):
        for d in self.docs :
            d.afficher()

    def rechercher(self, titre : str) :
        for d in self.docs :
            if d.titre == titre :
                return d
            
        return None
    
    