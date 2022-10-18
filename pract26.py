#Ejecutando programas externos desde tkinter
from tkinter import *
from tkinter import filedialog
import os
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")

def openfile():
    my_program=filedialog.askopenfilename()
    my_label.config(text=my_program)
    os.system('"%s"' % my_program)      #Al hacerlo de esta forma no debemos preocuparnos por los espacios que puedan existir en las rutas de los programas
btn=Button(root,text="Abrir",command=openfile)
btn.pack(pady=20)

my_label=Label(root,text="")
my_label.pack(pady=20)

root.mainloop()