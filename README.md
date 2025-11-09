
# 🧮 Héritage

## 📘 Description

Cette série de projets met en œuvre les principes fondamentaux de la programmation orientée objet, à travers des cas concrets de gestion d’entreprise et de bibliothèque :

- Héritage pour spécialiser les comportements selon les sous-types

- Polymorphisme via la redéfinition des méthodes (afficher, salaire_total)

- Encapsulation des données internes (ex. nom, salaire, titre, année)

- Agrégation d’objets : une bibliothèque contient plusieurs documents

- Méthodes spéciales (__str__) pour personnaliser l’affichage

- Organisation modulaire avec séparation des responsabilités

## 📂 Project Structure
````
projets/
├── Exercice 1/
│   ├── employe.py
│   ├── manager.py
│   ├── developpeur.py
│   └── test.py
├── Exercice 2/
│   ├── document.py
│   ├── livre.py
│   ├── magazine.py
│   ├── Bibliotheque.py
│   └── test.py
└── README.md
````


## ⚙️ Features

### **1.** . Entreprise – Système de calcul de salaires avec héritage 
Classe Employe

- Attributs d’instance : nom, salaire_base

Méthodes :

- salaire_total() : retourne le salaire de base

- __str__() : retourne une chaîne avec le nom et le salaire total

Classe Developpeur

- Attribut d’instance : technologie

Méthodes :

- salaire_total() : retourne le salaire de base + bonus selon la technologie

Classe Manager

- Attribut d’instance : prime

Méthode :

- salaire_total() : retourne le salaire de base + prime

### **2.** Bibliotheque – Gestion documentaire avec recherche et affichage polymorphe 
Classe Document

- Attributs d’instance : titre, annee

Méthode :

- afficher() : affiche le titre et l’année

Classe Livre

- Attribut d’instance : auteur

Méthode :

- afficher() : affiche le titre, l’auteur et l’année

Classe Magazine

- Attribut d’instance : numero

Méthode :

- afficher() : affiche le titre, le numéro et l’année

Classe Bibliotheque

- Attributs : __nom, docs (liste de documents)

Méthodes :

- ajouter_docs(doc) : ajoute un document à la bibliothèque

- afficher_docs() : affiche tous les documents

- rechercher(titre) : retourne le document correspondant au titre
## 🖥️ Example Execution


### Séparer proprement une classe unique :

### Mini-bibliothèque géométrique : 

### Création d’une librairie statique (.a) ou partagée (.so) :

### Classe template et fichier d’en-tête uniquement :


## 💡 Concepts Practiced

- Utiliser l’héritage pour factoriser et spécialiser les comportements

- Appliquer le polymorphisme pour unifier l’appel des méthodes (afficher, salaire_total)

- Organiser les classes dans des modules séparés pour une meilleure lisibilité

- Encapsuler les données et respecter la cohérence des objets

- Manipuler des collections d’objets hétérogènes dans une même structure
## 🧑‍💻 Author

- 👤 Agouram Hassan
- 🏫 Programmation orientée objet : Python
- 🎓 Instructor	Mr.LACHGAR
- 📅 09	novembre 2025
