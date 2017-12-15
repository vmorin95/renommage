from Action import *
import os

class Renommage (Action) :
    #constructeur
    def __init__(self, nomdurepertoire, regle):
        Action.__init__(self,nomdurepertoire,regle)
    #méthode renommer fichier
    def rename_files(self):
        original, renommer = self.simule()
        j = 0
        for i in range(len(original)):
            os.rename(os.path.join(self.nomdurepertoire, original[i]),
                      os.path.join(self.nomdurepertoire, renommer[i]))
            j += 1
        return j