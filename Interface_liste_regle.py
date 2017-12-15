from Listeregle import *
from Interface import *
from tkinter import*

class Interface_liste_regle:
    #constructeur
    def __init__(self, master, interface_renommage):
        self.master = master
        self.interface_renommage = interface_renommage

        self.prompt_label = Label(self.master, text = 'Choisissez une règle à appliquer :')
        self.prompt_label.place(x = 50, y = 10)

        self.Listeregle = Listeregle([])
        self.Listeregle.charger('test.txt')

        self.regles = self.Listeregle.get_regles()
        self.value = IntVar()
        i = 0
        j = 40

        for regle in self.regles:
            ttk.Radiobutton(self.master, text = regle.get_nomregle(), variable = self.value, value = i).place(x = 50, y = j)
            i += 1
            j += 20

        self.apply_button = Button(self.master, text = 'Appliquer', command = self.apply)
        self.apply_button.place(relx = 0.25, rely = 0.9)

        self.close_button = Button(self.master, text = 'Annuler', command = self.close)
        self.close_button.place(relx = 0.5, rely = 0.9)
    #méthode apply
    def apply(self):
        regle = self.regles[self.value.get()]
        MAPPING = {'' : 'Aucune', 'letter' : 'Lettre', 'number' : 'Chiffre'}
        self.interface_renommage.ChoixAmorce.set(MAPPING[regle.get_amorce()])
        self.interface_renommage.entree_apartirde.delete(0, END)
        self.interface_renommage.entree_apartirde.insert(0, regle.get_apartirde())
        self.interface_renommage.entree_prefixe.delete(0, END)
        self.interface_renommage.entree_prefixe.insert(0, regle.get_prefixe())

        if isinstance(regle.get_file_name(), str):
            self.interface_renommage.value.set('rename')
            self.interface_renommage.entree_nomfichier.delete(0, END)
            self.interface_renommage.entree_nomfichier.insert(0, regle.get_file_name())
        else:
            self.interface_renommage.value.set('original')
            self.interface_renommage.entree_nomfichier.delete(0, END)

        self.interface_renommage.entree_postfixe.delete(0, END)
        self.interface_renommage.entree_postfixe.insert(0, regle.get_postfixe())

        string = ''
        i = 1
        for ext in regle.get_extension():
            string += ext
            if i < len(regle.get_extension()):
                string += ','
            i += 1
        self.interface_renommage.entree_exConcernee.delete(0, END)
        self.interface_renommage.entree_exConcernee.insert(0, string)

        self.master.destroy()
    #méthode fermer
    def fermer(self):
        self.master.destroy()