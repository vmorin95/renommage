from Regle import *

# Classe utilisée pour charger et conserver la liste des règles

class ListeRegle:
    #constructeur
    def __init__(self, regles):
        self.regles = regles

    #getter et setter
    def get_regles(self):
        return self.regles

    def set_regles(self, regles):
        self.regles = regles

    # Méthodes

    #str
    def __str__(self):
        string = ''
        for r in self.regles:
            string += r.__str__() + '\n \n'
        return string

    #sauvegarder tout
    def sauvegarder_tout(self, nomfichier):
        with open(nomfichier, 'w', encoding='utf-8') as file:
            string = ''
            for r in self.regles:
                string += r.get_amorce() + ',' + r.get_apartirde() + ',' + r.get_prefixe() + ',' + \
                         str(r.get_nomfichier()) + ',' + r.get_postfixe() + ',' + r.get_nomregle() + '/'
                i = 1
                for e in r.get_extension():
                    string += e
                    if i < len(r.get_extension()):
                        string += ','
                    i += 1
                string += '\n'
            file.write(string)

    #sauvegarder en ajout
    def sauvegarder(self, nomfichier, regle):
        with open(nomfichier, 'a', encoding='utf-8') as file:
            string = regle.get_amorce() + ',' + regle.get_apartirde() + ',' + regle.get_prefixe() + ',' + \
                      str(regle.get_nomfichier()) + ',' + regle.get_postfixe() + ',' + regle.get_nomregle() + '/'
            i = 1
            for e in regle.get_extension():
                string += e
                if i < len(regle.get_extension()):
                    string += ','

                i += 1
            string += '\n'
            file.write(string)

    #charger
    def charger(self, nomfichier):
        with open(nomfichier, 'r', encoding='utf-8') as file:
            lignes = file.readlines()
        lignes = [x.strip() for x in lignes]
        for ligne in lignes:
            split = ligne.split('/')
            nomfichier_attributs = split[0].split(',')
            extension = split[1].split(',')

            if nomfichier_attributs[3] == 'True':
                nomfichier_attributs[3] = True
            elif nomfichier_attributs[3] == 'False':
                nomfichier_attributs[3] = False

            regle = Regle(nomfichier_attributs[0], nomfichier_attributs[1], nomfichier_attributs[2],
                        nomfichier_attributs[3], nomfichier_attributs[4], extension, nomfichier_attributs[5])

            self.regles.append(regle)

    #ajouter une règle
    def ajouter_regle(self, nomfichier, regle):
        self.regles.append(regle)
        self.sauvegarder(nomfichier, regle)
