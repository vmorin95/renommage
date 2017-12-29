import tkinter as tk
from MainApplication import *

# Démarreur de l'application

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()


if __name__ == '__main__':
    main()
