from tkinter import messagebox
from Interface import *
from ListeRegle import *

# Classe utilisée lors de l'ouverture de l'interface de la création de règle

class InterfaceRegle(Interface):
    #constructeur
    def __init__(self, master):
        Interface.__init__(self, master)

        self.titre_label = Label(self.master, text = 'Créer une règle')
        self.titre_label.place(x = 225, y = 15)

        self.nom_label = Label(self.master, text = 'Nom de la règle')
        self.nom_label.place(x = 55, y = 53)

        self.bouton_cree = Button(self.master, text = 'Créer', command = self.cree)
        self.bouton_cree.place(x = 450, y = 225)

    # Méthodes

    #création de la règle
    def cree(self):
        regle = self.get_regle()
        regle.set_nomregle(self.nom_entree.get())
        listeregle = ListeRegle([])
        listeregle.ajouter_regle('Panda.ini', regle)
        self.master.destroy()
        messagebox.showinfo('Règle enregistrée', 'Règle enregistrée')
