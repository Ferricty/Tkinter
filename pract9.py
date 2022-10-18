from cgi import print_directory
from tkinter import *

from PIL import Image, ImageTk


root = Tk()
root.title("Ejemplo")
root.iconbitmap("bruja.ico")
root.geometry("450x600")

#--------------------------------Ventanas Emergentes------------------------

# def open():
#     global miimagen
#     top = Toplevel()
#     top.title("Segunda Ventana")
#     top.iconbitmap("bruja.ico")
#     miimagen = ImageTk.PhotoImage(Image.open("bruja.png"))
#     texto=Label(top,image=miimagen).pack()
#     btn2=Button(top,text="Close Window",command=top.destroy).pack()
    
# btn=Button(root,text="Abrir otra ventana", command=open).pack()



#--------------------------------Slide------------------------


# vertical = Scale(root, from_=0, to=400)
# vertical.pack()

# horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
# horizontal.pack()

# my_label=Label(root,text=horizontal.get()).pack()

# def slide():
#     #my_label=Label(root,text=horizontal.get()).pack()
#     root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

# my_btn=Button(root,text="Click Me!", command=slide).pack()


#--------------------------------Drop Down Boxes------------------------


# options=[
#     "Monday",
#     "Tuesday",
#     "Wednesday",
#     "Thursday",
#     "Friday",
#     "Saturday",
#     "Sunday"
# ]
# clicked=StringVar()
# clicked.set(options[0])
# def show():
#     milabel= Label(root,text=clicked.get()).pack()

# drop=OptionMenu(root, clicked, *options)
# drop.pack()

# btn=Button(root, text="Show selection",command=show).pack()


#------------------------------Databases-------------------------ver pract7BBDD y pract8BBDD
import sqlite3

con=sqlite3.connect('agenda.db')  #Create a database or connect to one

c= con.cursor()            #Create cursor

estado=0     
# c.execute('''
#           CREATE TABLE agenda(
#               nombre txt,
#               apellidos txt,
#               direccion txt,
#               municipio txt,
#               zipcode integer
#           )
#           ''')





#La de abajo es la actual

# c.execute('''
#     CREATE TABLE agenda(
#         ID INTEGER PRIMARY KEY AUTOINCREMENT,
#         Nombre VARCHAR(20),
#         Apellidos VARCHAR(20),
#         Direccion VARCHAR(50),
#         Municipio VARCHAR(20),
#         Telefono INTEGER(10)
#     )
#     ''')

global f_nombre
global f_apellidos
global f_direccion
global f_municipio
global f_telefono

f_nombre=Entry(root,width=30)
f_nombre.grid(row=0,column=1,padx=20,pady=(20,0))

f_apellidos=Entry(root,width=30)
f_apellidos.grid(row=1,column=1,padx=20)

f_direccion=Entry(root,width=30)
f_direccion.grid(row=2,column=1,padx=20)

f_municipio=Entry(root,width=30)
f_municipio.grid(row=3,column=1,padx=20)

f_telefono=Entry(root,width=30)
f_telefono.grid(row=4,column=1,padx=20)

f_delete=Entry(root,width=30)
f_delete.grid(row=9,column=1,padx=(0,10))

l_nombre=Label(root, text="Nombre")
l_nombre.grid(row=0,column=0,padx=20,pady=(20,0))

l_apellidos=Label(root, text="Apellidos")
l_apellidos.grid(row=1,column=0,padx=20)

l_direccion=Label(root, text="Direccion")
l_direccion.grid(row=2,column=0,padx=20)

l_municipio=Label(root,text="Municipio")
l_municipio.grid(row=3,column=0,padx=20)

l_telefono=Label(root, text="Teléfono")
l_telefono.grid(row=4,column=0,padx=20)

l_delete=Label(root, text="ID")
l_delete.grid(row=9,column=0,padx=(10,0))
#Create submit button
def submit():
    global estado
    if estado==1:
        con=sqlite3.connect('agenda.db')    #Create a database or connect to one
        c= con.cursor()                     #Create cursor
        c.execute("""UPDATE agenda SET
                'nombre'=:nombre,
                'apellidos'=:apellidos,
                'direccion'=:direccion,
                'municipio'=:municipio,
                'Telefono'=:Telefono
                WHERE oid = :oid""",
                {
                'nombre':f_nombre.get(),
               'apellidos':f_apellidos.get(),
               'direccion':f_direccion.get(),
               'municipio':f_municipio.get(),
               'Telefono':f_telefono.get(),
               'oid':f_delete.get()
               })                         #Insertar en tabla
        
        #Limpiar cuadros de texto
        f_nombre.delete(0,END)
        f_apellidos.delete(0,END)
        f_direccion.delete(0,END)
        f_municipio.delete(0,END)
        f_telefono.delete(0,END)
        
        con.commit()
        c.close()
        estado=0
        mostrar()
        return
    if f_nombre.get()=="" or f_apellidos.get()==""  or f_direccion.get()==""  or f_municipio.get()==""  or f_telefono.get()=="" :
        top = Toplevel()
        top.title("ERROR")
        top.iconbitmap("bruja.ico")
        top.geometry("300x100")
        warnlbl=Label(top, text="Por favor rellene todos los campos",pady=20,padx=20)
        warnlbl.pack()
        return 
    con=sqlite3.connect('agenda.db')    #Create a database or connect to one
    c= con.cursor()                     #Create cursor
    # c.execute("INSERT INTO agenda VALUES(:nombre,:apellidos,:direccion,:municipio,:zipcode)",
    #           {'nombre':f_nombre.get(),
    #            'apellidos':f_apellidos.get(),
    #            'direccion':f_direccion.get(),
    #            'municipio':f_municipio.get(),
    #            'zipcode':f_telefono.get()
    #            }
    #           )                         #Insertar en tabla
    c.execute("INSERT INTO agenda VALUES(NULL,:nombre,:apellidos,:direccion,:municipio,:zipcode)",
              {'nombre':f_nombre.get(),
               'apellidos':f_apellidos.get(),
               'direccion':f_direccion.get(),
               'municipio':f_municipio.get(),
               'zipcode':f_telefono.get()
               }
              )
    #Limpiar cuadros de texto
    f_nombre.delete(0,END)
    f_apellidos.delete(0,END)
    f_direccion.delete(0,END)
    f_municipio.delete(0,END)
    f_telefono.delete(0,END)
        
    con.commit()
    c.close()

def borrar():
    if f_delete.get()=="":
        top1 = Toplevel()
        top1.title("ERROR")
        top1.iconbitmap("bruja.ico")
        top1.geometry("300x100")
        warnlbl=Label(top1, text="Debe introducir la ID del campo a eliminar",pady=20,padx=20)
        warnlbl.pack()
        return 
    
    global querylabel
    con=sqlite3.connect('agenda.db')    #Create a database or connect to one
    c= con.cursor()                     #Create cursor
    
    #DELETE RECORD
    #c.execute("DELECT FROM agenda WHERE oid=PLACEHOLDER")
    c.execute("DELETE FROM agenda WHERE oid = " + f_delete.get())
     
    con.commit()
    c.close()
    mostrar()
    
def mostrar():
    global querylabel
    
    con=sqlite3.connect('agenda.db')    #Create a database or connect to one
    c= con.cursor()                     #Create cursor
    c.execute("SELECT *, oid FROM agenda")
    registros=c.fetchall()
    print_records=""
    for registro in registros:
        #print_records += str(registro[0]) + " "+ str(registro[1]) +" "+ str(registro[4]) +"\t"+"\n"     #muestra campos de posicion 0,1,4
        #print_records += str(registro[0]) + "\t"+ str(registro[1]) + "\t"+ str(registro[-1]) +"\n"
        print_records += str(registro[0]) + "\t" +"\t"+str(registro[1]) +"\t"+ "\t"+str(registro[2]) +"\t"+ "\t"+str(registro[-2])+"\n"
    querylabel=Label(root, text=print_records)
    tablapropiedades=Label(root, text="ID\tNombre\t \t Apellidos\t \tTeléfono")
    tablapropiedades.grid(row=11,column=0, columnspan=2,pady=(20,0))  
    querylabel.grid(row=12,column=0, columnspan=2)    
    con.commit()
    c.close()
    
def filtrar():
    global f_nombre_filtrar
    global f_telefono_filtrar
    ventana_filtrar=Toplevel()
    ventana_filtrar.title("Criterios de búsqueda")
    ventana_filtrar.geometry("600x600")
    
    f_nombre_filtrar=Entry(ventana_filtrar,width=30)
    f_nombre_filtrar.grid(row=0,column=1,padx=20,pady=(20,0))

    f_telefono_filtrar=Entry(ventana_filtrar,width=30)
    f_telefono_filtrar.grid(row=2,column=1,padx=20)

    l_nombre_filtrar=Label(ventana_filtrar, text="Nombre")
    l_nombre_filtrar.grid(row=0,column=0,padx=20,pady=(20,0))

    l_telefono_filtrar=Label(ventana_filtrar, text="Teléfono")
    l_telefono_filtrar.grid(row=2,column=0,padx=20)
    def searchfiltros():
        global f_nombre_filtrar
        global f_telefono_filtrar
        con=sqlite3.connect('agenda.db')    #Create a database or connect to one
        c= con.cursor()                     #Create cursor
        if f_nombre_filtrar.get()!="" and f_telefono_filtrar.get()!="":
            c.execute("SELECT * FROM agenda WHERE Nombre = '{}' AND Telefono = {} ".format(f_nombre_filtrar.get(),f_telefono_filtrar.get()))
        elif f_nombre_filtrar.get()!=""and f_telefono_filtrar.get()=="":
            c.execute("SELECT * FROM agenda WHERE Nombre = '{}'".format(f_nombre_filtrar.get()))
        elif f_nombre_filtrar.get()==""and f_telefono_filtrar.get()!="":
            c.execute("SELECT * FROM agenda WHERE Telefono = {}".format(f_telefono_filtrar.get()))
        else:
            top1 = Toplevel()
            top1.title("ERROR")
            top1.iconbitmap("bruja.ico")
            top1.geometry("300x100")
            warnlbl=Label(top1, text="Establezca criterios de búsqueda",pady=20,padx=20)
            warnlbl.pack()
        registros=c.fetchall()
        print_records=""
        for registro in registros:
            #print_records += str(registro[0]) + " "+ str(registro[1]) +" "+ str(registro[4]) +"\t"+"\n"     #muestra campos de posicion 0,1,4
            #print_records += str(registro[0]) + "\t"+ str(registro[1]) + "\t"+ str(registro[-1]) +"\n"
            print_records += str(registro[0]) + "\t" +"\t"+str(registro[1]) +"\t"+ "\t"+str(registro[2]) +"\t"+ "\t"+str(registro[-1])+"\n"
        
        querylabel=Label(ventana_filtrar, text=print_records)
        tablapropiedades=Label(ventana_filtrar, text="ID\tNombre\t \t Apellidos\t \tTeléfono")
        tablapropiedades.grid(row=3,column=0, columnspan=2,pady=(20,0))  
        querylabel.grid(row=4,column=0, columnspan=2)    
        con.commit()
        c.close()
    buscar_btn=Button(ventana_filtrar,text="Buscar", command=searchfiltros)
    buscar_btn.grid(row=8,column=1,padx=(0,0),ipadx=10)
def editar():
    f_nombre.delete(0,END)
    f_apellidos.delete(0,END)
    f_direccion.delete(0,END)
    f_municipio.delete(0,END)
    f_telefono.delete(0,END)
    global estado
    if f_delete.get()=="" :
        top = Toplevel()
        top.title("ERROR")
        top.iconbitmap("bruja.ico")
        top.geometry("250x80")
        warnlbl=Label(top, text="Por favor escriba la ID\n del registro a modificar",pady=20,padx=20)
        warnlbl.pack()
        return 
    con=sqlite3.connect('agenda.db')    #Create a database or connect to one
    c= con.cursor()                     #Create cursor
    
    c.execute("SELECT * FROM agenda WHERE oid =" + f_delete.get())   #Query database
    records=c.fetchall()
    
    for record in records:
        f_nombre.insert(0,record[1])
        f_apellidos.insert(0,record[2])
        f_direccion.insert(0,record[3])
        f_municipio.insert(0,record[4])
        f_telefono.insert(0,record[5])
    
    con.commit()
    c.close()
    estado=1
    
#Creando submit button        
submit_btn=Button(root,text="Agregar Registro", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)
#Creando query button 
submit_btn=Button(root,text="Mostrar Registros", command=mostrar)
submit_btn.grid(row=7,column=0)
#Boton de filtros de busqueda
filtro_btn=Button(root,text="Filtrar Registros", command=filtrar)
filtro_btn.grid(row=7,column=1)

#Creando delete button
borrar_btn=Button(root,text="Borrar registro de ID", command=borrar)
borrar_btn.grid(row=8,column=0,pady=10,padx=(50,0),ipadx=10)
#Creando update button
editar_btn=Button(root,text="Editar registro de ID", command=editar)
editar_btn.grid(row=8,column=1,padx=(0,0),ipadx=10)


con.commit()
c.close()

root.mainloop()
    