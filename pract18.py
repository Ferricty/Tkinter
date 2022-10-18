#config te permite cambiar contenido de los label
from tkinter import *

from matplotlib.pyplot import text
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")

def algo():
    mylabel.config(text="Texto cambiado",bg="red")
    root.config(bg="red")
    mybtn.config(text="Contenido cambiado",state=DISABLED)
global mybtn
global mylabel    
mylabel=Label(root,text="Texto original")
mylabel.pack(pady=10)
mybtn=Button(root,text="Click Me!",command=algo)
mybtn.pack(pady=15)
root.mainloop()