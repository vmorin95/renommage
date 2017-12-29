from tkinter import *
from tkinter import ttk
from Regle import *

# Classe utilisée pour la disposition des pages InterfaceRenommer et InterfaceRegle

class Interface:
    #constructeur
    def __init__(self, master):

        #nom de repetoire
        self.master = master
        self.nom_entree = Entry(self.master)
        self.nom_entree.configure(width = 40)
        self.nom_entree.place(x = 150, y = 55)

        #amorce
        self.amorce_label = Label(self.master, text = 'Amorce')
        self.amorce_label.place(x = 35, y = 125)
        self.combo_var = StringVar()
        self.combo_var.set('Aucune')
        self.amorce_box = ttk.Combobox(self.master, textvariable = self.combo_var, state = 'readonly', values = ['Aucune', 'Lettre', 'Chiffre'])
        self.amorce_box.configure(width = 8)
        self.amorce_box.place(x = 25, y = 150)
        self.MAPPING = {'Aucune' : '', 'Lettre' : 'letter', 'Chiffre' : 'number'}

        #apartirde
        self.apartirde_label = Label(self.master, text = 'A partir de')
        self.apartirde_label.place(x = 27, y = 225)
        self.apartirde_entree = Entry(self.master)
        self.apartirde_entree.configure(width = 9)
        self.apartirde_entree.place(x = 27, y = 250)

        #prefixe
        self.prefixe_label = Label(self.master, text = 'Préfixe')
        self.prefixe_label.place(x = 140, y = 125)
        self.prefixe_entree = Entry(self.master)
        self.prefixe_entree.configure(width = 10)
        self.prefixe_entree.place(x = 129, y = 150)

        #nomfichier
        self.nomfichier_label = Label(self.master, text = 'Nom du fichier')
        self.nomfichier_label.place(x = 225, y = 125)
        self.radio_var = StringVar()
        self.radio_var.set('original')
        self.nomfichier_radiobouton1 = ttk.Radiobutton(self.master, text = 'Nom original', variable = self.radio_var, value = 'original')
        self.nomfichier_radiobouton2 = ttk.Radiobutton(self.master, variable = self.radio_var, value = 'renomme')
        self.nomfichier_radiobouton1.place(x = 215, y = 150)
        self.nomfichier_radiobouton2.place(x = 215, y = 180)
        self.nomfichier_entree = Entry(self.master)
        self.nomfichier_entree.configure(width = 12)
        self.nomfichier_entree.place(x = 235, y = 180)

        #postfixe
        self.postfixe_label = Label(self.master, text = 'Postfixe')
        self.postfixe_label.place(x = 350, y = 125)
        self.postfixe_entree = Entry(self.master)
        self.postfixe_entree.configure(width = 10)
        self.postfixe_entree.place(x = 342, y = 150)

        #extension
        self.extension_label = Label(self.master, text = 'Extension(s) concernée(s)')
        self.extension_label.place(x = 440, y = 125)
        self.extension_entree = Entry(self.master)
        self.extension_entree.configure(width = 20)
        self.extension_entree.place(x = 447, y = 150)

        #image
        self.image = PhotoImage(file = 'Pandalogo.png')
        self.image_label = Label(self.master, image = self.image)
        self.image_label.place(x = 450, y = 20)

    # Méthodes

    #récupération des règles
    def get_regle(self):
        amorce = self.MAPPING[self.amorce_box.get()]
        apartirde = self.apartirde_entree.get()
        prefixe = self.prefixe_entree.get()

        if self.radio_var.get() == 'original':
            nomfichier = True
        else:
            nomfichier = self.nomfichier_entree.get()

        postfixe = self.postfixe_entree.get()
        extension = self.extension_entree.get().split(',')

        return Regle(amorce, apartirde, prefixe, nomfichier, postfixe, extension)

    #suppression des données saisies dans les différentes entrées
    def effacer(self):
        self.nom_entree.delete(0, END)
        self.combo_var.set('Aucune')
        self.apartirde_entree.delete(0, END)
        self.prefixe_entree.delete(0, END)
        self.radio_var.set('original')
        self.nomfichier_entree.delete(0, END)
        self.postfixe_entree.delete(0, END)
        self.extension_entree.delete(0, END)
        self.nom_entree.focus_set()
