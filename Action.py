import os
import string

class Action :
    #constructeur
    def __init__(self, nomdurepertoire, regle):
        self.nomdurepertoire = nomdurepertoire
        self.regle = regle

    #getter
    def get_nomdurepertoire(self):
        return self.nomdurepertoire

    def get_regle(self):
        return self.regle

    #setter
    def set_nomdurepertoire(self, nomdurepertoire):
        self.nomdurepertoire = nomdurepertoire

    def set_regle(self, regle):
        self.regle =regle


    #str
    def __str__(self):
        return self.nomdurepertoire + self.regle

    # methode
    #convertion des lettres en nombres
    def conv_alphabet_en_nombre(self, alphabet):
        num = 0
        for nomb in alphabet:
            if nomb in string.ascii_letters:
                num = num * 26 + (ord(nomb.upper()) - ord('A')) + 1
        return num

    # convertion des nombres en lettres
    def conv_nombre_en_alphabet(self, int):
        str = ""
        while int > 0:
            int, remainder = divmod(int - 1, 26)
            str = chr(65 + remainder) + str
        return str

    #simule
    def simule(self):
        if self.regle.get_extention() == '':
            original_nomfichiers = [nfich for nfich in os.listdir(self.nomdurepertoire)]
        else:
            original_nomfichiers = [nfich for nfich in os.listdir(self.nomdurepertoire)
                                   if nfich.endswith(tuple(self.regle.get_extention()))]

        renommer_nomfichiers = []

        if self.regle.get_apartirde() == '' or self.regle.get_amorce() == '':
            apartirde = 0
        elif self.regle.get_amorce() == 'lettre':
            apartirde = self.conv_alphabet_en_nombre(self.regle.get_apartirde())
        elif self.regle.get_amorce() == 'nombre':
            nombre = self.regle.get_from_init()
            if nombre.isdigit():
                apartirde = int(nombre)
            else:
                apartirde = 0

        for original_nomfichier in original_nomfichiers:
            renommer_nomfichier, extension = os.path.splitext(original_nomfichier)

            if isinstance(self.regle.get_nomfichier(),str):
                renommer_nomfichier = self.regle.get_nomfichier()

            if self.regle.get_prefixe() != '':
                renommer_nomfichier = self.regle.get_prefixe() + renommer_nomfichier

            if self.regle.get_postfixe() != '':
                renommer_nomfichier = self.regle.get_prefixe() + renommer_nomfichier

            apartirde += 1

            if self.regle.get_amorce() == '':
                amorce = ''
            elif self.regle.get_amorce() == 'letter':
                amorce = self.conv_nombre_en_alphabet(apartirde)
            elif self.regle.get_amorce() == 'number':
                amorce = '{0}'.format(str(apartirde).zfill(3))

            if amorce != '':
                renommer_nomfichier = amorce + renommer_nomfichier

            renommer_nomfichier = renommer_nomfichier + extension

            renommer_nomfichiers.append(renommer_nomfichier)

        return original_nomfichiers, renommer_nomfichiers


