import csv

def importCSV(fichier : str, separateur = ";"):
    tCSV = csv.DictReader(open(fichier,'r'), delimiter = separateur)
    tableau = []
    for ligne in tCSV:
        tableau.append(dict(ligne))
    return tableau

def exportCSV(tableau : list, fichier : str):
    header = tableau[0].keys()
    fichierCSV = csv.DictWriter(open(fichier, 'w'), fieldnames = header)
    fichierCSV.writeheader()
    for ligne in tableau:
        fichierCSV.writerow(ligne)
    return None

def filtrerLigne(tableau : list, critere : str, valeur : str):
    filtrerTableau = []
    for dico in tableau:
        if(dico[critere] == valeur):
            filtrerTableau.append(dico)
    return filtrerTableau
    #return [filtrerTableau for dico in tableau if dico[critere] == valeur]


def filtrerColonne(tableau : list, listeCriteres : list):
    filtrerTableau = []
    for dico in tableau:
        dicoFiltrer = {}
        for (cle,valeur) in dico.items():
            if cle in listeCriteres:
                dicoFiltrer[cle]=valeur
        filtrerTableau.append(dicoFiltrer)
    return filtrerTableau
    #return [{cle:dico[cle] for cle in dico.keys() if cle in listeCriteres} for dico in tableau]

def triTable(tableau: list, critere: str, decroissant = False ):
    return sorted(tableau, key=lambda k: k['dep'], reverse=decroissant)


def jointure(table1, table2, descripteur):
    tableFinale = []
    for dictionnaire1 in table1: # dictionnaire1 est une variable locale de boucle
        nouveauDico = {}
        for dictionnaire2 in table2:
            if dictionnaire1[descripteur] == dictionnaire2[descripteur]:
                for (cle1, valeur1) in dictionnaire1.items():
                    nouveauDico[cle1] = valeur1
                for (cle2, valeur2) in dictionnaire2.items():
                    nouveauDico[cle2] = valeur2
                # print(nouveauDico)
                tableFinale.append(nouveauDico)
    return tableFinale


