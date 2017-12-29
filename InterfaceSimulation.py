from tkinter import *
from tkinter import messagebox

# Classe utilisée pour afficher la simulation de renommage des fichiers et les renommer

class InterfaceSimulation:
    #constructeur
    def __init__(self, master, action_renommer, interface_renommer):
        self.master = master
        self.action_renommer = action_renommer
        self.interface_renommer = interface_renommer

        self.prompt_label = Label(self.master, text = 'Etes-vous sûr de vouloir renommer ces fichiers ?')
        self.prompt_label.place(x = 50, y = 10)

        self.original, self.renommer = self.action_renommer.simulation()
        j = 40
        for i in range(len(self.original)):
            Label(self.master, text = self.original[i] + ' -> ' + self.renommer[i]).place(x = 50, y = j)
            j += 20

        self.renomme_bouton = Button(self.master, text = 'Oui', command = self.renomme)
        self.renomme_bouton.place(relx = 0.4, rely = 0.9)

        self.fermer_bouton = Button(self.master, text = 'Non', command = self.fermer)
        self.fermer_bouton.place(relx = 0.5, rely = 0.9)

    # Méthodes

    #renommage des fichiers
    def renomme(self):
        seen = set()
        duplicates = set(x for x in self.renommer if x in seen or seen.add(x))
        if len(duplicates) == 0:
            nombre_fichiers = self.action_renommer.renommer_fichiers()
            self.master.destroy()
            messagebox.showinfo('Fichiers renommés', 'Nombre de fichiers renommés : ' + str(nombre_fichiers))
            self.interface_renommer.effacer()
        else:
            messagebox.showinfo('Avertissement', 'Opération impossible : \n'
                                                 'Un ou plusieurs fichiers ont le même nom et la même extension')

    def fermer(self):
        self.master.destroy()
