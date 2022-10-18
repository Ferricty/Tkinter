#Trabajando con timers y construyendo reloj
from tkinter import *
import time
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")


def clock():
    hour=time.strftime("%I")            #H para darla en forato 24h, I formato 12 horas
    minute=time.strftime("%M")
    second=time.strftime("%S")
    day=time.strftime("%A")
    am_pm=time.strftime("%p")
    my_label.config(text=hour+":"+minute+":"+second+" "+am_pm)
    my_label.after(1000,clock)
    my_label2.config(text=day)

def update():
    my_label.config(text="New text")
    
my_label=Label(root,text="Old text")
my_label.pack(pady=20)
my_label2=Label(root,text="")
my_label2.pack(pady=20)
#my_label.after(2000,update)         #Despues de 2000 ms activa la funcion. NO SE LE PONE PARENTESIS AL LLAMAR A LA FUNCION
clock()


root.mainloop()