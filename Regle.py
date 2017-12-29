# Classe utilisée pour encapsuler les différentes entrées de données des formulaires des interfaces

class Regle:
    #constructeur
    def __init__(self, amorce, apartirde, prefixe, nomfichier, postfixe, extension, nomregle=''):
        self.amorce = amorce
        self.apartirde = apartirde
        self.prefixe = prefixe
        self.nomfichier = nomfichier
        self.postfixe = postfixe
        extension = [x.strip() for x in extension]
        self.extension = extension
        self.nomregle = nomregle

    #getter et setter
    def get_amorce(self):
        return self.amorce


    def set_amorce(self, amorce):
        self.amorce = amorce


    def get_apartirde(self):
        return self.apartirde


    def set_apartirde(self, apartirde):
        self.apartirde = apartirde


    def get_prefixe(self):
        return self.prefixe


    def set_prefixe(self, prefixe):
        self.prefixe = prefixe


    def get_nomfichier(self):
        return self.nomfichier


    def set_nomfichier(self, nomfichier):
        self.nomfichier = nomfichier


    def get_postfixe(self):
        return self.postfixe


    def set_postfixe(self, postfixe):
        self.postfixe = postfixe


    def get_extension(self):
        return self.extension


    def set_extension(self, extension):
        self.extension = extension


    def get_nomregle(self):
        return self.nomregle

    def set_nomregle(self, nomregle):
        self.nomregle = nomregle

    # Méthodes

    #str
    def __str__(self):
        string = "Amorce : '" + self.amorce + "' \n" \
                 "A partir de : '" + self.apartirde + "' \n" \
                 "Prefixe : '" + self.prefixe + "' \n" \
                 "Nom fichier : '" + str(self.nomfichier) + "' \n" \
                 "Postfixe : '" + self.postfixe + "' \n" \
                 "Nom regle : '" + self.nomregle + "' \n" \
                 "Extension : '"
        i = 1
        for e in self.extension:
            string += e
            if i < len(self.extension):
                string += ', '
            i += 1
        string += "'"
        return string
