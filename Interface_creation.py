from Interface import *
from Listeregle import *


#classe de l'interface création
class Interface_creation(Interface):
    #constructeur
    def __init__(self, master):
        Interface.__init__(self,master)

        self.but1 = Button(master, text="Créer", width=20)
        self.but1.place(x=500, y=300, height=40)

        self.Lab1 = Label(master, text ="Créer une règle")
        self.Lab1.place(x=400, y=40)
        self.Lab2 = Label(master, text="Nom de la règle")
        self.Lab2.place(x=200, y=80)
        self.valu2 = StringVar()
        self.entree_regle = Entry(master, textvariable=self.valu2, width=50)
        self.entree_regle.place(x=350, y=80, height=20)
    #méthode création
    def creation(self):
        regle = self.get_regle()
        regle.set_nomregle(self.entree_regle.get())
        listeregle = Listeregle([])
        listeregle.add_rule('test.txt', regle)
        self.master.destroy()