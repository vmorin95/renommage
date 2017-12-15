from Interface import *
from Renommage import *
from Simule import *

#classe de l'interface de renommage
class Interface_renommage (Interface):
    def __init__(self, master):
        Interface.__init__(self, master)

        self.but1 = Button(master, text="Renommage", width=20)
        self.but1.place(x=500, y=300, height=40)

        self.Lab1 = Label(master, text ="Renommer en lots")
        self.Lab1.place(x=400, y=40)

        self.Lab2 = Label(master, text="Nom du répertoire")
        self.Lab2.place(x=200, y=80)
        self.valu = StringVar()
        self.entree_regle = Entry(master, textvariable=self.valu, width=50)
        self.entree_regle.place(x=350, y=80, height=20)
    #méthode de renommage
    def rename(self):
        nomdurepertoire = self.entree_nomfichier.get()
        if os.path.isdir(nomdurepertoire):
            regle = self.get_regle()
            renommer_act = Renommage(nomdurepertoire, regle)
            self.new_window = Toplevel(self.master)
            self.new_window.title('Prévisualisation')
            self.new_window.minsize(width=375, height=300)
            self.simulation_frame = Simule(self.new_window, renommer_act, self)
        else:
            messagebox.showinfo('Info',"nom existant")
