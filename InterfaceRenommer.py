from Interface import *
from Renommer import *
from InterfaceSimulation import *

# Classe utilisée lors de l'ouverture de l'interface du renommage des fichiers


class InterfaceRenommer(Interface):
    #constructeur
    def __init__(self, master):
        Interface.__init__(self, master)

        self.titre_label = Label(self.master, text = 'Renommer en lots')
        self.titre_label.place(x = 225, y = 15)

        self.nom_label = Label(self.master, text = 'Chemin du répertoire')
        self.nom_label.place(x = 25, y = 53)

        self.renomme_bouton = Button(self.master, text = 'Renommer', command = self.renomme)
        self.renomme_bouton.place(x = 450, y = 225)

    # Méthodes

    #renommage des fichiers
    def renomme(self):
        nomrepertoire = self.nom_entree.get()
        if os.path.isdir(nomrepertoire):
            regle = self.get_regle()
            action_renommer = Renommer(nomrepertoire, regle)
            self.nouvelle_fenetre = Toplevel(self.master)
            self.nouvelle_fenetre.title('Prévisualisation')
            self.nouvelle_fenetre.minsize(width = 375, height = 300)
            self.simulation_frame = InterfaceSimulation(self.nouvelle_fenetre, action_renommer, self)
        else:
            messagebox.showinfo('Info', "Le répertoire n'existe pas")
