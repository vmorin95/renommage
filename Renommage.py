from Action import *

# Classe utilisée pour renommer les fichiers dans le système

class Renommer(Action):
    #constructeur
    def __init__(self, nomrepertoire, regle):
        Action.__init__(self, nomrepertoire, regle)

    # Méthodes

    #renommer les fichiers
    def renommer_fichiers(self):
        original, renommer = self.simulation()
        j = 0
        for i in range(len(original)):
            os.rename(os.path.join(self.nomrepertoire, original[i]),
                      os.path.join(self.nomrepertoire, renommer[i]))
            j += 1
        return j
