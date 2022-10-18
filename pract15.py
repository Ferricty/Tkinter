from tkinter import *
from tkinter import colorchooser
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")
def color():
    mycolor=colorchooser.askcolor()[1]  #Se devuelven dos elementos un diccionario RGB y el segundo elemento es el color en hexadecimal
    
    mylabel=Label(root,text=mycolor).pack(pady=10)
    mylabel2=Label(root,text="You picked a color!", font=("Helvetica",32),bg=mycolor).pack(pady=10)
btn=Button(root,text="Pick a color",command=color).pack()
root.mainloop()