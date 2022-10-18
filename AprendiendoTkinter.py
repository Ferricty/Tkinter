from tkinter import *
import tkinter
from typing import final

root=Tk()

def clic():
    myLabel=Label(root,text="Hola {}".format(e.get()))
    myLabel.pack()

# label1=Label(root,text="Hello")

# label2=Label(root,text="Mi nombre es Frank")

# label1.grid(row=0,column=0)
# label2.grid(row=1,column=0)



e=Entry(root, width=25, bg="gray", fg="blue",)
e.pack()

# Entry
# width ancho
# bg y fg similar a botones
# 
mybutton=Button(root,text="Enter your name",command=clic,padx=20,bg="#002487",fg="yellow",border="4px")    
mybutton.pack()


#Buttons
# command es para llamar una funcion. No se utilizan parentesis al final
# padx padding
# text escribir texto del boton 
# background or bg indicar color de relleno del boton
# fg color de fuente del texto del boton
# border indica el grosor del borde




root.mainloop()