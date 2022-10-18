from tkinter import *
from turtle import right

from matplotlib.pyplot import fill, text

root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")

#Creando frame y scrollbar
my_frame=Frame(root)
my_scrollbar=Scrollbar(my_frame,orient=VERTICAL)


# Selectmode SINGLE, MULTIPLE, BROWSE, EXTENDED
# -Por defecto el selectmode es SINGLE;
# -MULTIPLE permite la seleccion de multiples elementos al hacer clic
# -EXTENDED similar a multiple pero es necesario presionar shift para seleccionar varios
# -BROWSE mover elementos es necesario codigo extra 
#mylistbox=Listbox(my_frame,width=50,yscrollcommand=my_scrollbar.set)
mylistbox=Listbox(my_frame,width=50,yscrollcommand=my_scrollbar.set,selectmode=MULTIPLE)

my_scrollbar.config(command=mylistbox.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
mylistbox.pack(pady=15)
my_frame.pack()
mylistbox.insert(END,"This is an item")
mylistbox.insert(END,"Second item")
l=["One","Two","Three","Two","Three","Two","Three","Two","Three","Two","Three","Two","Three","Two","Three","Two","Three","Two","Three","Two","Three","Two","Three","Two","Three","Two","Three"]
for i in l:
    mylistbox.insert(END,i)
    
def delete():
    mylistbox.delete(ANCHOR)
    mylabel.config(text='')
def select():
    mylabel.config(text=mylistbox.get(ANCHOR))  #ANCHOR se refiere a la seleccionada
    
def delete_all():
    mylistbox.delete(0,END)

def select_all():
    result=''
    r=mylistbox.curselection()    #devuelve indice de los elementos seleccionados
    for item in r:
        result+=result+str(mylistbox.get(item))+"\n"
    mylabel.config(text=result)
def delete_multiple():
    for item in reversed(mylistbox.curselection()):     #es necesario recorrer la lista en sentido contrario porque los indices cambian
        mylistbox.delete(item)   
btn=Button(root,text="delete",command=delete).pack(pady=10)
btn2=Button(root,text="select",command=select).pack(pady=10)
btn3=Button(root,text="delete all",command=delete_all).pack(pady=10)
btn4=Button(root,text="select all",command=select_all).pack(pady=10)
btn5=Button(root,text="delete multiple",command=delete_multiple).pack(pady=10)
global mylabel
mylabel=Label(root,text='')
mylabel.pack(pady=10)
root.mainloop()