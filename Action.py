import os
import string

# Classe utilisée lors de la simulation du renommage de fichiers

class Action:
    #constructeur
    def __init__(self, nomrepertoire, regle):
        self.nomrepertoire = nomrepertoire
        self.regle = regle

    #getter et setter
    def get_nomrepertoire(self):
        return self.nomrepertoire

    def set_nomrepertoire(self, nomrepertoire):
        self.nomrepertoire = nomrepertoire

    def get_regle(self):
        return self.regle

    def set_regle(self, regle):
        self.regle = regle

    # Méthode

    #str
    def __str__(self):
        return "Directory name : '" + self.nomrepertoire + "' \n" + self.regle.__str__()

    #convertion de nombre en lettre
    def conv_nombre_en_alphabet(self, int):
        string = ""
        while int > 0:
            int, remainder = divmod(int - 1, 26)
            string = chr(65 + remainder) + string
        return string

    #convertion de lette en nombre
    def conv_alphabet_en_nombre(self, alphabet):
        num = 0
        for c in alphabet:
            if c in string.ascii_letters:
                num = num * 26 + (ord(c.upper()) - ord('A')) + 1
        return num

    #simulation de renommage de fichiers
    def simulation(self):
        if self.regle.get_extension() == '':
            original_nom_fichiers = [nomfichier for nomfichier in os.listdir(self.nomrepertoire)]
        else:
            original_nom_fichiers = [nomfichier for nomfichier in os.listdir(self.nomrepertoire)
                                   if nomfichier.endswith(tuple(self.regle.get_extension()))]

        renommer_nom_fichiers = []

        if self.regle.get_apartirde() == '' or self.regle.get_amorce() == '':
            apartirde = 0
        elif self.regle.get_amorce() == 'letter':
            apartirde = self.conv_alphabet_en_nombre(self.regle.get_apartirde())
        elif self.regle.get_amorce() == 'number':
            number = self.regle.get_apartirde()
            if number.isdigit():
                apartirde = int(number)
            else:
                apartirde = 0

        for original_nom_fichier in original_nom_fichiers:
            renommer_nom_fichier, extension = os.path.splitext(original_nom_fichier)

            if isinstance(self.regle.get_nomfichier(), str):
                renommer_nom_fichier = self.regle.get_nomfichier()

            if self.regle.get_prefixe() != '':
                renommer_nom_fichier = self.regle.get_prefixe() + renommer_nom_fichier

            if self.regle.get_postfixe() != '':
                renommer_nom_fichier = renommer_nom_fichier + self.regle.get_postfixe()

            apartirde += 1

            if self.regle.get_amorce() == '':
                amorce = ''
            elif self.regle.get_amorce() == 'letter':
                amorce = self.conv_nombre_en_alphabet(apartirde)
            elif self.regle.get_amorce() == 'number':
                amorce = '{0}'.format(str(apartirde).zfill(3))

            if amorce != '':
                renommer_nom_fichier = amorce + renommer_nom_fichier

            renommer_nom_fichier = renommer_nom_fichier + extension

            renommer_nom_fichiers.append(renommer_nom_fichier)

        return original_nom_fichiers, renommer_nom_fichiers
