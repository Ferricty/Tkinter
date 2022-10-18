from cgitb import text
from tkinter import *

root=Tk()

def imprimir():
    
    if varopcion.get()==1:
        etiqueta.config(text="Masculino")
    else:
        etiqueta.config(text="Femenino")

varopcion=IntVar()
Label(root, text="Genero").pack()
Radiobutton(root,text="Masculino", variable=varopcion, value=1, command=imprimir).pack()
Radiobutton(root,text="Femenino", variable=varopcion, value=2, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()

root.mainloop()
