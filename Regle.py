class Regle :
    #constructeur
    def __init__(self, amorce, apartirde, prefixe, nomfichier, postfixe, extension, nomregle = ''):
        self.amorce = amorce
        self.apartirde = apartirde
        self.prefixe = prefixe
        self.nomfichier = nomfichier
        self.postfixe = postfixe
        self.extension = extension
        self.nomregle = nomregle

    #getter
    def get_amorce(self):
       return self.amorce

    def get_apartirde(self):
        return self.apartirde

    def get_prefixe(self):
        return self.prefixe

    def get_nomfichier(self):
        return self.nomfichier

    def get_postfixe(self):
        return self.postfixe

    def get_extension(self):
        return self.extension

    def get_nomregl(self):
        return self.nomregle

    #setter
    def set_amorce(self, amorce):
        self.amorce = amorce

    def set_apartirde(self, apartirde):
        self.apartirde = apartirde

    def set_prefixe(self, prefixe):
        self.prefixe = prefixe

    def set_nomfichier(self, nomfichier):
        self.nomfichier = nomfichier

    def set_postfixe(self, postfixe):
        self.postfixe = postfixe

    def set_extension(self, extension):
        self.extension = extension

    def set_nomregle(self, nomregle):
        self.nomregle = nomregle

    #methode str
    def __str__(self):
        string = self.amorce + self.apartirde + self.prefixe + self.nomfichier + self.postfixe + self.nomregle + "\n"

        i = 1
        for ext in self.extension:
            string += ext
            if i < len(self.extension):
                string += ','
            i += 1
        string += "'"
        return string


