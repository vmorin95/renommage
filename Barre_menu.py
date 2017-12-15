from Interface_creation import *
from Interface_liste_regle import *
from tkinter import messagebox

#classe barre de menu
class Barre_menu:
    #constructeur
    def __init__(self, master, renomme):
        self.master = master
        self.renomme = renomme
        self.menubar = Menu(master)
        self.Menuregle = Menu(self.menubar, tearoff=0)
        self.Menuinfo = Menu(self.master, tearoff=0)
        self.menubar.add_cascade(label='Règles', menu=self.Menuregle)
        self.Menuregle.add_command(label='Lister', command = self.liste_regle)
        self.Menuregle.add_command(label='Créer', command = self.cree_regle)
        self.menubar.add_cascade(label='?', menu=self.Menuinfo)
        self.Menuinfo.add_command(label='A propos de', command = self.info)
        master.config(menu=self.menubar)

    #méthode qui génère une interface quand on clique sur Lister
    def liste_regle(self):
        self.new_window_rl = Toplevel(self.master)
        self.new_window_rl.title('Liste des règles')
        self.new_window_rl.minsize(width=300, height=300)
        self.listeregle = Interface_liste_regle(self.new_window_rl, self.renomme)

    #méthode qui génère une interface quand on clique sur Créer
    def cree_regle(self):
        self.new_window_r = Toplevel(self.master)
        self.new_window_r.title('Créer une règle')
        self.new_window_r.resizable(width=False, height=False)
        self.new_window_r.minsize(width=1000, height=600)
        self.creeregle = Interface_creation(self.new_window_r)

    #information sur le logiciel
    def info(self):
        messagebox.showinfo("Logiciel de renommage")