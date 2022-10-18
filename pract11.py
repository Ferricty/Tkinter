from tkinter import *
from PIL import ImageTk,Image
from matplotlib import use
import mysql.connector
import csv
from tkinter import ttk
from tkinter import messagebox
root=Tk()
root.title("BBDD MySQL")
root.iconbitmap("bruja.ico")
root.geometry("400x500")


#Connect to Mysql
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="ferricty",)

#print(mydb)        #Comprobar conexion con mysql. Como no da error se creo satisfactoriamente


mycursor=mydb.cursor()      #Crear cursor e inicializarlo

mycursor.execute("CREATE DATABASE IF NOT EXISTS Ferricty")   #Crear base de datos

#mycursor.execute("SHOW DATABASES")  #Comprobar si fue creada

#Para eliminar la tabla
# mycursor.execute("DROP TABLE Clientes")


# for db in mycursor:
#     print(db)
   
#        Nota aclaratoria Precio DECIMAL(10,2),   Indica que va a ser un decimal con 10 caracteres y 2 cifras decimales   

#Creacion de la tabla    
mycursor.execute("CREATE TABLE IF NOT EXISTS Clientes(\
    nombre VARCHAR(255),\
    primer_apellido VARCHAR(255),\
    segundo_apellido VARCHAR(255),\
    telefono INT(10),\
    precio DECIMAL(10,2),\
    user_id INT AUTO_INCREMENT PRIMARY KEY)")

#Para alterar la tabla

# mycursor.execute("ALTER TABLE Clientes ADD(\
#     email VARCHAR(255),\
#     direccion VARCHAR(255),\
#     ciudad VARCHAR(255),\
#     metodo_de_pago VARCHAR(50),\
#     codigo_de_descuento VARCHAR(255))")


mycursor.execute("SELECT * FROM Clientes")
#print(mycursor.description) #mostrando la tabla     es una lista que contiene varias tuplas con las propiedades de los campos

# for algo in mycursor.description:
#     print(algo)
    
l_titulo=Label(root, text="Ferricty Database", font=("Helvetica",16))
l_titulo.grid(row=0,column=0,columnspan=2,pady=10,padx=(100,0))

#Creando formulario principal para entrar datos de clientes
l_nombre=Label(root, text="Nombre").grid(row=1,column=0,sticky=W,padx=60)
l_primer_apellido=Label(root, text="Primer Apellido").grid(row=2,column=0,sticky=W,padx=60)
l_segundo_apellido=Label(root, text="Segundo Apellido").grid(row=3,column=0,sticky=W,padx=60)
l_telefono=Label(root, text="Telefono").grid(row=4,column=0,sticky=W,padx=60)
l_precio=Label(root, text="Precio").grid(row=5,column=0,sticky=W,padx=60)
l_email=Label(root, text="Email").grid(row=6,column=0,sticky=W,padx=60)
l_direccion=Label(root, text="Dirección").grid(row=7,column=0,sticky=W,padx=60)
l_ciudad=Label(root, text="Ciudad").grid(row=8,column=0,sticky=W,padx=60)
l_metodo_de_pago=Label(root, text="Método de Pago").grid(row=9,column=0,sticky=W,padx=60)
l_codigo_de_descuento=Label(root, text="Código de descuento").grid(row=10,column=0,sticky=W,padx=60)

#Creando cuadros de entrada de datos
f_nombre=Entry(root)
f_nombre.grid(row=1,column=1,pady=5)
f_primer_apellido=Entry(root)
f_primer_apellido.grid(row=2,column=1,pady=5)
f_segundo_apellido=Entry(root)
f_segundo_apellido.grid(row=3,column=1,pady=5)
f_telefono=Entry(root)
f_telefono.grid(row=4,column=1,pady=5)
f_precio=Entry(root)
f_precio.grid(row=5,column=1,pady=5)
f_email=Entry(root)
f_email.grid(row=6,column=1,pady=5)
f_direccion=Entry(root)
f_direccion.grid(row=7,column=1,pady=5)
f_ciudad=Entry(root)
f_ciudad.grid(row=8,column=1,pady=5)
f_metodo_de_pago=Entry(root)
f_metodo_de_pago.grid(row=9,column=1,pady=5)
f_codigo_de_descuento=Entry(root)
f_codigo_de_descuento.grid(row=10,column=1,pady=5)


#Clear formulario
def clear_form():
    f_nombre.delete(0,END)
    f_primer_apellido.delete(0,END)
    f_segundo_apellido.delete(0,END)
    f_telefono.delete(0,END)
    f_precio.delete(0,END)
    f_email.delete(0,END)
    f_direccion.delete(0,END)
    f_ciudad.delete(0,END)
    f_metodo_de_pago.delete(0,END)
    f_codigo_de_descuento.delete(0,END)



#Agregar
def add_cliente():
    mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="ferricty",)
    mycursor=mydb.cursor() 
    sql_command = "INSERT INTO clientes (nombre, primer_apellido, segundo_apellido, telefono, precio, email, direccion, ciudad, metodo_de_pago, codigo_de_descuento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #sql_command = "INSERT INTO clientes (nombre, primer_apellido, segundo_apellido, telefono, precio) VALUES (%s, %s, %s,%s, %s)"
    values = (f_nombre.get(), f_primer_apellido.get(), f_segundo_apellido.get(), f_telefono.get(), f_precio.get(), f_email.get(), f_direccion.get(), f_ciudad.get(), f_metodo_de_pago.get(), f_codigo_de_descuento.get())
    #values = (f_nombre.get(), f_primer_apellido.get(), f_segundo_apellido.get(), f_telefono.get(), f_precio.get())
    mycursor.execute(sql_command, values)
    
    #Commit changes
    mydb.commit()
    clear_form()

def write_to_csv(resultado):
    with open('clientes.csv','a',newline="") as f:
        w=csv.writer(f, dialect="excel")
        w.writerows(resultado)

def buscar_clientes():
    search_clientes=Tk()
    search_clientes.title("Buscar los clientes")
    search_clientes.geometry("1000x600")
    search_clientes.iconbitmap("bruja.ico")
    
    def editar_ahora(id,index):
        pass
    
    
    
    def buscar_ahora():
        selected = drop.get()
        if selected=="Search by...":
            messagebox.showerror("Error","Olvidaste seleccionar tu criterio de búsqueda")
        elif selected=="Primer Apellido":
            sql="SELECT * FROM Clientes WHERE primer_apellido = %s"
            
            
        elif selected=="Email Address":
            sql="SELECT * FROM Clientes WHERE email = %s"
            
        elif selected=="Nombre":
            sql="SELECT * FROM Clientes WHERE nombre = %s"
            
        else:
            sql="SELECT * FROM Clientes WHERE nombre = %s"
            
        searched=f_busqueda.get()
        mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="ferricty",)
        mycursor=mydb.cursor() 
        name=(searched,)
        result=mycursor.execute(sql,name)
        result=mycursor.fetchall()
        
        if not result:
            result="No encontrado..."
        else:
            for index,x in enumerate(result):
                num=0
                index+=3
                id_reference=str(x[5])
                edit_button=Button(search_clientes, text="Editar " + id_reference, command = editar_ahora(id_reference,index))
                edit_button.grid(row = index, column = num, padx = (10,0), pady = 5)
                for y in x:
                    l_search=Label(search_clientes, text=y)
                    l_search.grid(row=index, column=num+1, padx=(10,0),pady=5)
                    num+=1
        print(index)
        index+=1
        l_nombre2=Label(search_clientes, text="Nombre")
        l_nombre2.grid(row=index+1,column=0,sticky=W,padx=60,pady=10)
        l_primer_apellido2=Label(search_clientes, text="Primer Apellido")
        l_primer_apellido2.grid(row=index+2,column=0,sticky=W,padx=60)
        l_segundo_apellido2=Label(search_clientes, text="Segundo Apellido")
        l_segundo_apellido2.grid(row=index+3,column=0,sticky=W,padx=60)
        l_telefono2=Label(search_clientes, text="Telefono")
        l_telefono2.grid(row=index+4,column=0,sticky=W,padx=60)
        l_precio2=Label(search_clientes, text="Precio")
        l_precio2.grid(row=index+5,column=0,sticky=W,padx=60)
        l_email2=Label(search_clientes, text="Email")
        l_email2.grid(row=index+6,column=0,sticky=W,padx=60)
        l_direccion2=Label(search_clientes, text="Dirección")
        l_direccion2.grid(row=index+7,column=0,sticky=W,padx=60)
        l_ciudad2=Label(search_clientes, text="Ciudad")
        l_ciudad2.grid(row=index+8,column=0,sticky=W,padx=60)
        l_metodo_de_pago2=Label(search_clientes, text="Método de Pago")
        l_metodo_de_pago2.grid(row=index+9,column=0,sticky=W,padx=60)
        l_codigo_de_descuento2=Label(search_clientes, text="Código de descuento")
        l_codigo_de_descuento2.grid(row=index+10,column=0,sticky=W,padx=60)
        id_label=Label(search_clientes, text="ID")
        id_label.grid(row=index+11,column=0,sticky=W,padx=60)
        #Creando cuadros de entrada de datos
        f_nombre2=Entry(search_clientes)
        f_nombre2.grid(row=index+1,column=1,pady=10)
        f_primer_apellido2=Entry(search_clientes)
        f_primer_apellido2.grid(row=index+2,column=1,pady=5)
        f_segundo_apellido2=Entry(search_clientes)
        f_segundo_apellido2.grid(row=index+3,column=1,pady=5)
        f_telefono2=Entry(search_clientes)
        f_telefono2.grid(row=index+4,column=1,pady=5)
        f_precio2=Entry(search_clientes)
        f_precio2.grid(row=index+5,column=1,pady=5)
        f_email2=Entry(search_clientes)
        f_email2.grid(row=index+6,column=1,pady=5)
        f_direccion2=Entry(search_clientes)
        f_direccion2.grid(row=index+7,column=1,pady=5)
        f_ciudad2=Entry(search_clientes)
        f_ciudad2.grid(row=index+8,column=1,pady=5)
        f_metodo_de_pago2=Entry(search_clientes)
        f_metodo_de_pago2.grid(row=index+9,column=1,pady=5)
        f_codigo_de_descuento2=Entry(search_clientes)
        f_codigo_de_descuento2.grid(row=index+10,column=1,pady=5)
            
    #Label
    l_busqueda=Label(search_clientes, text="Buscar")
    l_busqueda.grid(row=0,column=0,padx=10,pady=10)
    #Formulario
    f_busqueda=Entry(search_clientes)
    f_busqueda.grid(row=0,column=1,padx=10,pady=10)
    #Boton de buscar_clientes
    buscar_btn=Button(search_clientes,text="Buscar",command=buscar_ahora)
    buscar_btn.grid(row=1,column=0,padx=10,pady=10)
    #Drop down box
    drop=ttk.Combobox(search_clientes, values=["Search by...","Nombre","Primer Apellido","Email Address","Customer ID"])
    drop.current(0)
    drop.grid(row=0,column=2)
   
def listar_clientes():
    ventana_listar_clientes=Tk()
    ventana_listar_clientes.title("Listar todos los clientes")
    ventana_listar_clientes.geometry("800x600")
    ventana_listar_clientes.iconbitmap("bruja.ico")
    mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="ferricty",)
    mycursor=mydb.cursor() 
    mycursor.execute("SELECT * FROM Clientes") 
    resultado=mycursor.fetchall()
    for index,x in enumerate(resultado):
        num=0
        for y in x:
            l_mostrar=Label(ventana_listar_clientes, text=y)
            l_mostrar.grid(row=index, column=num, padx=(10,0))
            num+=1
    csv_btn=Button(ventana_listar_clientes, text="Guardar en un CSV",command = lambda: write_to_csv(resultado))        
    csv_btn.grid(row=index+1,column=0)
            
    #Commit changes
    mydb.commit()

#Customer button
addcustomer_btn=Button(root, text="Add client",command=add_cliente)
addcustomer_btn.grid(row=11,column=0,padx=(60,0),pady=10,sticky=W)
#Clear
clear_btn=Button(root, text="Clear Fields",command=clear_form)
clear_btn.grid(row=11,column=1,pady=10,sticky=W)
#Listar clientes
lst_btn=Button(root, text="Show clients",command=listar_clientes)
lst_btn.grid(row=12,column=0,pady=10,padx=(60,0),sticky=W)
#Buscar clientes
lst_btn=Button(root, text="Buscar",command=buscar_clientes)
lst_btn.grid(row=12,column=1,pady=10,sticky=W)
root.mainloop()
