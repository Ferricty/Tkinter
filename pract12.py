#Formas de eliminar label

#nombre_label.pack_forget()
#nombre_label.grid_forget()
#nombre_label.destroy()
from tkinter import *

root=Tk()
root.title("BBDD MySQL")
root.iconbitmap("bruja.ico")
root.geometry("400x500")

my_btn=Button(root,text="Click Me!")
#my_btn.bind(event,action)
def clicker(event):
    #l_mylabel=Label(root,text="You clicked the button"+" "+str(event.x)+" "+str(event.y)+" ") event.x y event.y devuelven coordenadas del mouse
    l_mylabel=Label(root,text="You press this key: "+ event.char)
    l_mylabel.pack()

#"<Button-1>" pulsar clic izquierdo
#"<Button-2>" pulsar rueda del raton
#"<Button-3>" pulsar clic derecho
#"<Enter>" Ejecuta el evento si el mouse entra al widget
#"<Leave>" Ejecuta el evento si el mouse sale del widget
#"<FocusIn>" Ejecuta el evento con TAB al ser seleccionado
#"<FocusIn>" Ejecuta el evento con TAB al dejar de ser seleccionado
#"<Return>" Ejecuta el evento con Enter al ser seleccionado
#"<Return>" Ejecuta el evento con cualquier tecla del teclado

my_btn.bind("<Key>",clicker)
my_btn.pack(pady=10)

root.mainloop()
