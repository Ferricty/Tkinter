from tkinter import *

root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")
#Trabajando con unicode el codigo se busca en wikipedia internet etc

mylabel2=Label(root,text="42"+u'\u00b0', font=("Helvetica",32)).pack(pady=10)

root.mainloop()