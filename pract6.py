from tkinter import *
from tkinter import filedialog

root=Tk()

def abrefichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="D:",filetypes=(("Ficheros de Excel","*.xlsx"),
                                                                                 ("Ficheros de texto","*.txt"),
                                                                                 ("Todos los ficheros","*.*")))
    print(fichero)
Button(root, text="Abrir fichero",command=abrefichero).pack()

root.mainloop()