from tkinter import *
from tkinter import ttk
from ListeRegle import *

# Classe utilisée pour saisir la liste de la regle que l'on veut séléctionner

class InterfaceListeRegle:
    #constructeur
    def __init__(self, master, interface_renommer):
        self.master = master
        self.interface_renommer = interface_renommer

        self.prompt_label = Label(self.master, text = 'Choisissez une règle à appliquer :')
        self.prompt_label.place(x = 50, y = 10)

        self.listeregle = ListeRegle([])
        self.listeregle.charger('Panda.ini')

        self.regles = self.listeregle.get_regles()
        self.radio_var = IntVar()
        i = 0
        j = 40

        for regle in self.regles:
            ttk.Radiobutton(self.master, text = regle.get_nomregle(), variable = self.radio_var, value = i).place(x = 50, y = j)
            i += 1
            j += 20

        self.bouton_appli = Button(self.master, text = 'Appliquer', command = self.appli)
        self.bouton_appli.place(relx = 0.25, rely = 0.9)

        self.bouton_fermer = Button(self.master, text = 'Annuler', command = self.fermer)
        self.bouton_fermer.place(relx = 0.5, rely = 0.9)

    # Méthodes

    #récupération des éléments saisie dans InterfaceRegle
    def appli(self):
        regle = self.regles[self.radio_var.get()]
        MAPPING = {'' : 'Aucune', 'letter' : 'Lettre', 'number' : 'Chiffre'}
        self.interface_renommer.combo_var.set(MAPPING[regle.get_amorce()])
        self.interface_renommer.apartirde_entree.delete(0, END)
        self.interface_renommer.apartirde_entree.insert(0, regle.get_apartirde())
        self.interface_renommer.prefixe_entree.delete(0, END)
        self.interface_renommer.prefixe_entree.insert(0, regle.get_prefixe())

        if isinstance(regle.get_nomfichier(), str):
            self.interface_renommer.radio_var.set('renomme')
            self.interface_renommer.nomfichier_entree.delete(0, END)
            self.interface_renommer.nomfichier_entree.insert(0, regle.get_nomfichier())
        else:
            self.interface_renommer.radio_var.set('original')
            self.interface_renommer.nomfichier_entree.delete(0, END)

        self.interface_renommer.postfixe_entree.delete(0, END)
        self.interface_renommer.postfixe_entree.insert(0, regle.get_postfixe())

        string = ''
        i = 1
        for e in regle.get_extension():
            string += e
            if i < len(regle.get_extension()):
                string += ','
            i += 1
        self.interface_renommer.extension_entree.delete(0, END)
        self.interface_renommer.extension_entree.insert(0, string)

        self.master.destroy()

    #fermture
    def fermer(self):
        self.master.destroy()
