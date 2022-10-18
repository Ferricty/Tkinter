#Dibujando formas con Canvas y darle movimiento
from tkinter import *


root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("500x500")

my_canvas=Canvas(root,width=300,height=200,bg="white")
my_canvas.pack(pady=20)
#Creando lineas
#my_canvas.create_line(x1,y1,x2,y2,fil"color")
      
my_canvas.create_line(0,100,300,100,fill="red")
my_canvas.create_line(150,0,150,200,fill="red")

#Rectangulo en este casso x1,y1 son las coordenadas Top Left y x2,y2 Bottom Right
my_canvas.create_rectangle(0,0,200,200,fill="pink")

my_canvas.create_oval(100,100,200,200,fill="blue")



root.mainloop()