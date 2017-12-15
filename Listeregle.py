from Regle import *

class Listeregle:
    #constructeur
    def __init__(self, regles):
        self.regles = regles

    #getter
    def get_regles(self):
        return self.regles

    #setter
    def set_regles(self, regles):
        self.regles = regles

    #methode
    #str
    def __str__(self):
        str = ''
        for regle in self.regles:
            str += regle.__str__() + '\n'
        return str

    #sauvegarder
    def sauvegarder_en_ajout(self, nomfichier, regle):
        with open(nomfichier, 'a', encoding='utf-8') as file:
            string = regle.get_amorce() + ',' + regle.get_apartirde() + ',' + regle.get_prefix() + ',' + \
                str(regle.get_nomfichier()) + ',' + regle.get_postfixe() + regle.get_nomregle() +'/'
        i = 1
        for ext in regle.get_extension():
            string += ext
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
            nomfichier_attributes = split[0].split(',')
            extension = split[1].split(',')

            if nomfichier_attributes[3] == 'True':
                nomfichier_attributes[3] = True
            elif nomfichier_attributes[3] == 'False':
                nomfichier_attributes[3] = False

            regle = Regle(nomfichier_attributes[0], nomfichier_attributes[1], nomfichier_attributes[2],
                          nomfichier_attributes[3], nomfichier_attributes[4], extension, nomfichier_attributes[5])
            self.regles.append(regle)
