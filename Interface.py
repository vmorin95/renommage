from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from Regle import*

class Interface:
    #constructeur
    def __init__(self, master):
        self.master = master

        #préfixe
        self.Lab4 = Label(master, text="Préfixe")
        self.Lab4.place(x=120, y=200)
        self.value2 = StringVar()
        self.entree_prefixe = Entry(master, textvariable=self.value2, width=15)
        self.entree_prefixe.place(x=100, y=230, height=20)

        #postfixe
        self.Lab6 = Label(master, text="Postfixe")
        self.Lab6.place(x=400, y=200)
        self.value3 = StringVar()
        self.entree_postfixe = Entry(master, textvariable=self.value3, width=15)
        self.entree_postfixe.place(x=400, y=230, height=20)

        #extention concernée
        self.Lab7 = Label(master, text="Extention concernée")
        self.Lab7.place(x=500, y=200)
        self.value4 = StringVar()
        self.entree_exConcernee = Entry(master, textvariable=self.value4, width=15)
        self.entree_exConcernee.place(x=500, y=230, height=20)

        #apartirde
        self.Lab8 = Label(master, text="Apartirde")
        self.Lab8.place(x=20, y=300)
        self.value5 = StringVar()
        self.entree_apartirde = Entry(master, textvariable=self.value5, width=15)
        self.entree_apartirde.place(x=20, y=330, height=20)

        #nom du fichier
        self.Lab5 = Label(master, text="Nom du fichier")
        self.Lab5.place(x=250, y=200)
        self.value = StringVar()
        self.entree_nomfichier = Entry(master, textvariable=self.value, width=30)
        self.radioBut1 = ttk.Radiobutton(master, text="Original", variable =self.value, value ='origine')
        self.radioBut2 = ttk.Radiobutton(master, textvariable=self.entree_nomfichier, variable=self.value, value='renommer')
        self.radioBut1.place(x=250,y=250)
        self.radioBut2.place(x=250,y=290)
        self.entree_nomfichier.place(x=270, y=290, height =20)

        #amorce
        self.Lab3 = Label(master, text="Amorce")
        self.Lab3.place(x=20, y=200)
        self.amorceMenu= StringVar()
        self.listeAmorce = ('Aucune', 'Lettre', 'Chiffre')
        self.ChoixAmorce = ttk.Combobox(master, textvariable=self.amorceMenu, values=self.listeAmorce)
        self.ChoixAmorce.place(x=20,y=230, width=60)
        self.MAPPING = {'Aucune': '', 'Lettre': 'lettre', 'Chiffre': 'chiffre'}

        #image
        self.img = PhotoImage(file='image.png')
        self.imgLab = Label(self.master, image=self.img)
        self.imgLab.place(x=700, y=20)

    #méthode récupérer regles
    def get_regle(self):
        amorce = self.MAPPING[self.ChoixAmorce.get()]
        apartirde = self.entree_apartirde.get()
        prefixe = self.entree_prefixe.get()
        if self.value.get() == 'original':
            nomfichier = True
        else:
            nomfichier = self.entree_nomfichier.get()

        postfixe = self.entree_postfixe.get()
        extension = self.entree_exConcernee.get().split(',')

        return Regle(amorce, apartirde, prefixe, nomfichier, postfixe, extension)

