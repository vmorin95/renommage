from tkinter import *
from tkinter import messagebox

#classe de simulation
class Simule:
    def __init__(self, master, renommer_act, renomme):
        self.master = master
        self.renommer_act = renommer_act
        self.renomme = renomme

        self.prompt_label = Label(self.master, text = 'Etes-vous sûr de vouloir renommer ces fichiers ?')
        self.prompt_label.place(x = 50, y = 10)

        self.original, self.renommer = self.renommer_act.simule()
        j = 40
        for i in range(len(self.original)):
            Label(self.master, text = self.original[i] + ' -> ' + self.renommer[i]).place(x = 50, y = j)
            j += 20

        self.bouton_renommer = Button(self.master, text = 'Oui', command = self.renommer)
        self.bouton_renommer.place(relx = 0.4, rely = 0.9)

        self.fermer_bouton = Button(self.master, text = 'Non', command = self.fermer)
        self.fermer_bouton.place(relx = 0.5, rely = 0.9)
    #méthode de renommage
    def renommer(self):
        seen = set()
        duplicates = set(x for x in self.renommer if x in seen or seen.add(x))
        if len(duplicates) == 0:
            nb_files = self.renommer_act.rename_files()
            self.master.destroy()
            messagebox.showinfo('Fichiers renommés', 'Nombre de fichiers renommés : ' + str(nb_files))
            self.renomme.clear_form()
        else:
            messagebox.showinfo('Avertissement', 'Opération impossible')
    #méthode fermer
    def fermer(self):
        self.master.destroy()