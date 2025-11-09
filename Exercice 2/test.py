from document import Document
from livre import Livre
from magazine import Magazine
from Bibliotheque import Bibliotheque

bib = Bibliotheque("mon_bibliotheque")

l1 = Livre("1984", 1949, "George Orwell")
m1 = Magazine("Science & Vie", 2023, 456)
l2 = Livre("Le Petit Prince", 1943, "Antoine de Saint-Exupéry")

bib.ajouter_docs(l1)
bib.ajouter_docs(l2)
bib.ajouter_docs(m1)

bib.afficher_docs()

doc = bib.rechercher("1984")
if doc :
    doc.afficher()
else :
    print("document introuvable!")
