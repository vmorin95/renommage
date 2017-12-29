from InterfaceRegle import *
from InterfaceListeRegle import *

# Classe utilisée lors de l'affichage de la barre de menu dans l'interface

class BarreMenu:
    #constructeur
    def __init__(self, master, interface_renommer):
        self.master = master
        self.interface_renommer = interface_renommer

        self.barredemenu = Menu(self.master)
        self.menuregle = Menu(self.barredemenu, tearoff = 0)
        self.menuregle.add_command(label = 'Lister', command = self.ouvrir_interface_listeregle)
        self.menuregle.add_command(label = 'Créer', command = self.ouvrir_interface_regle)
        self.barredemenu.add_cascade(label = 'Règles', menu = self.menuregle)
        self.barredemenu.add_command(label = '?', command = self.Apropos)

        self.master.config(menu = self.barredemenu)

    # Méthode

    #ouverture de l'interface listeregle
    def ouvrir_interface_listeregle(self):
        self.fenetre_listeregle = Toplevel(self.master)
        self.fenetre_listeregle.title('Liste des règles')
        self.fenetre_listeregle.minsize(width = 300, height = 300)
        self.interface_listeregle = InterfaceListeRegle(self.fenetre_listeregle, self.interface_renommer)

    #ouverture de l'interface regle
    def ouvrir_interface_regle(self):
        self.fenetre_regle = Toplevel(self.master)
        self.fenetre_regle.title('Créer une règle')
        self.fenetre_regle.resizable(width = False, height = False)
        self.fenetre_regle.minsize(width = 600, height = 300)
        self.interface_regle = InterfaceRegle(self.fenetre_regle)

    #a propos de l'application
    def Apropos(self):
        messagebox.showinfo('A propos', "Logiciel développé par Victor Morin ")
