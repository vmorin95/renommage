from InterfaceRenommer import *
from BarreMenu import *

# Controleur de l'application

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title('Renommage')
        self.master.resizable(width = False, height = False)
        self.master.minsize(width = 600, height = 300)
        self.interface_renommer = InterfaceRenommer(self.master)
        self.barremenu = BarreMenu(self.master, self.interface_renommer)
