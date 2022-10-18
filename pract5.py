from tkinter import *
from tkinter import messagebox

root=Tk()

def infoadd():
    messagebox.showinfo("Esto es una ventana emergente", "Version 1.0")
    
def avisolicencia():
    messagebox.showwarning("Licencia", "Se encuentra bajo licencia")
    
def salir():
    # valor=messagebox.askquestion("Salir", "Deseas salir?")
    # if valor=="yes":
    #     root.destroy()
    
    valor=messagebox.askokcancel("Salir", "Deseas salir?")
    if valor==True:
        root.destroy()

def cerrardoc():
    valor=messagebox.askretrycancel("Reintentar", "Documento bloqueado no es posible cerrarlo")
    if valor==False:
        root.destroy()
        
        
barramenu=Menu()
root.config(menu=barramenu,width=300,height=300)

archivoMenu=Menu(barramenu, tearoff=0)
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar como...")
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrardoc)
archivoMenu.add_command(label="Salir", command=salir)

edicionMenu=Menu(barramenu)
ayudaMenu=Menu(barramenu, tearoff=0)
ayudaMenu.add_command(label="Acerca de...", command=infoadd)
ayudaMenu.add_command(label="Licencia", command=avisolicencia)
barramenu.add_cascade(label="Archivo",menu=archivoMenu)
barramenu.add_cascade(label="Editar",menu=edicionMenu)
barramenu.add_cascade(label="Ayuda",menu=ayudaMenu)
root.mainloop()