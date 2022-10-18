#Creando Calendario para seleccionar fecha
from tkinter import *
from tkcalendar import *
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")

cal=Calendar(root,selectmode="day",year=2020,month=8,day=27)
cal.pack(pady=20)

def grab_date():
    mylabel.config(text=cal.get_date())

mybtn=Button(root,text="Get Date",command=grab_date)
mybtn.pack(pady=20)
mylabel=Label(root,text="")
mylabel.pack(pady=20)


root.mainloop()