from Interface_renommage import *
from Barre_menu import *

#classe main de l'application
class MainApp:
    def __init__(self, master):
        self.master = master
        self.master.title('Renommage')
        self.master.resizable(width = False, height = False)
        self.master.minsize(width = 1000, height = 600)
        self.interface_renommage= Interface_renommage(self.master)
        self.Barremenu = Barre_menu(self.master, self.interface_renommage)

