#Cambiando tamaño de la ventana
from tkinter import *

root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("600x600")

def resize():
    w=900
    h=200
    #root.geometry(f"{w}x{h}")
    #root.geometry("{width}x{height}".format(height=h,width=w))      #Interesante
    root.geometry("%ix%i"% (w,h)) # %i significa que es entero

btn=Button(root,text="Resize",command=resize)
btn.pack(pady=20)
root.mainloop()