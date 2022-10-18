from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import time
import csv
import pandas as pd

def clock(frame,x,y):
    my_time=Label(frame,text="",bg="white",font=("Bahnschrift Condensed",13),fg="dark slate gray",bd=4,relief="groove",width=10)
    my_time.place(x=x,y=y)
    hour=time.strftime("%I")            #H para darla en forato 24h, I formato 12 horas
    minute=time.strftime("%M")
    second=time.strftime("%S")
    am_pm=time.strftime("%p")
    my_time.config(text=hour+":"+minute+":"+second+" "+am_pm)
    my_time.after(1000,clock)
    
def write_to_excel(resultado):
    l=[]
    for elements in resultado[1:]:
        (a,*restresultado)=elements
        l.append(restresultado)
    df=pd.DataFrame(l,columns=resultado[0][1:])
    df.to_excel("Estudiantes.xlsx",index=False)
    
def write_to_csv(resultado):    
    #El codigo de abajo convierte a csv
    with open('Estudiantes.csv','a',newline="") as f:
        w=csv.writer(f, dialect="excel")
        #Para que guarde los resultados en sus respectivas columnas es necesario hacer un bucle for
        for i in resultado:
            w.writerow(i)
def submit_estudiante():
    if f_nombre_completo.get()=="" or f_aula.get()==""  or f_correo.get()=="":
        top = Toplevel()
        top.title("ERROR")
        top.iconbitmap("bruja.ico")
        top.geometry("300x100")
        warnlbl=Label(top, text="Por favor rellene todos los campos",pady=20,padx=20)
        warnlbl.pack()
        return 
    con=sqlite3.connect('Escuela.db')  #Create a database or connect to one

    c= con.cursor()            #Create cursor   
    c.execute("INSERT INTO Estudiantes VALUES(NULL,:nombre_completo,:aula,:correo)",
              {'nombre_completo':f_nombre_completo.get(),
               'aula':f_aula.get(),
               'correo':f_correo.get()
               }
              )                       #Insertar en tabla

    #Limpiar cuadros de texto
    f_nombre_completo.delete(0,END)
    f_aula.delete(0,END)
    f_correo.delete(0,END)
        
    con.commit()
    c.close()

def aplicar_cambios(id_reference):
    con=sqlite3.connect('Escuela.db')    #Create a database or connect to one
    c= con.cursor()                     #Create cursor
    c.execute("""UPDATE Estudiantes SET
            'nombre_completo'=:nombre_completo,
            'aula'=:aula,
            'correo'=:correo
            WHERE oid = :oid""",
            {
            'nombre_completo':f_nombre_completo_top.get(),
            'aula':f_aula_top.get(),
            'correo':f_correo_top.get(),
            'oid':id_reference
            })                         #Insertar en tabla
    
    #Limpiar cuadros de texto
    f_nombre_completo_top.delete(0,END)
    f_aula_top.delete(0,END)
    f_correo_top.delete(0,END)
    
    con.commit()
    c.close()
    listar_student()





def editar_ahora(id_reference):
    print(id_reference)
    #print(id_reference)
    top=Toplevel(panel2_admin,bg=QuesColor)
    top.title("Editando registro de estudiante con ID "+ str(id_reference))
    top.iconbitmap("bruja.ico")
    top.geometry("400x200")
    label_nombre_completo_estudiante_top=Label(top,text="Nombre Completo",bg=QuesColor)
    label_nombre_completo_estudiante_top.grid(column=0,row=0,pady=(20,5),sticky=W,padx=40)
    global f_nombre_completo_top
    f_nombre_completo_top=Entry(top)
    f_nombre_completo_top.grid(column=1,row=0,pady=(20,5),sticky=E)
    
    label_aula_estudiante_top=Label(top,text="Aula del estudiante",bg=QuesColor)
    label_aula_estudiante_top.grid(column=0,row=1,sticky=W,pady=5,padx=40)
    global f_aula_top
    f_aula_top=Entry(top)
    f_aula_top.grid(column=1,row=1,sticky=E)
    
    label_correo_estudiante_top=Label(top,text="Correo del estudiante",bg=QuesColor)
    label_correo_estudiante_top.grid(column=0,row=2,sticky=W,pady=5,padx=40)
    global f_correo_top
    f_correo_top=Entry(top)
    f_correo_top.grid(column=1,row=2,pady=5,sticky=E)
    
    con=sqlite3.connect('Escuela.db')    #Create a database or connect to one
    c= con.cursor()                     #Create cursor
    
    c.execute("SELECT * FROM Estudiantes WHERE oid =" + str(id_reference))   #Query database
    records=c.fetchall()
    # #Insertando valores actuales en sus campos
    for record in records:
        f_nombre_completo_top.insert(0,str(record[1]))
        f_aula_top.insert(0,str(record[2]))
        f_correo_top.insert(0,str(record[3]))
    con.commit()
    c.close()
    submit_btn_estudiante_top=Button(top,text="Aplicar Cambios",command=lambda:aplicar_cambios(id_reference))
    submit_btn_estudiante_top.grid(column=1,row=4,pady=10)
    
    
    
def eliminar_ahora(id_reference):
    con=sqlite3.connect('Escuela.db')    #Create a database or connect to one
    c= con.cursor()                     #Create cursor
    
    c.execute("SELECT nombre_completo FROM Estudiantes WHERE oid =" + str(id_reference))
    registro=c.fetchall()
    print(registro)
    valor=messagebox.askyesno("Eliminar Registro "+str(id_reference),"¿Está seguro que desea eliminar de la base de datos al estudiante ?")
    if valor==True:
        #DELETE RECORD
        #c.execute("DELECT FROM agenda WHERE oid=PLACEHOLDER")
        c.execute("DELETE FROM Estudiantes WHERE oid = " + str(id_reference))
     
    con.commit()
    c.close()
    listar_student()
    
def clear_panel2():
    for widget in panel2_admin.winfo_children():
            widget.destroy()


def buscar_ahora():
    global l_mostrar
    for widget in panel2_admin.winfo_children():
        if widget not in [f_busqueda,buscar_btn_combo,buscar_btn]:
            widget.destroy()
    con=sqlite3.connect('Escuela.db')    #Create a database or connect to one
    c= con.cursor()                     #Create cursor 
    selected = buscar_btn_combo.get()
    l=[]
    if selected=="Buscar por...":
        messagebox.showerror("Error","Olvidaste seleccionar tu criterio de búsqueda")
    elif selected=="Nombre y Apellidos":
        c.execute("SELECT * FROM Estudiantes WHERE nombre_completo = '{}'".format(f_busqueda.get()))
        
    elif selected=="Aula":
        
        c.execute("SELECT * FROM Estudiantes WHERE aula = '{}'".format(f_busqueda.get()))
    else:
        c.execute("SELECT * FROM Estudiantes WHERE correo = '{}'".format(f_busqueda.get()))

    result=c.fetchall()
    result.insert(0,("ID","Nombre y Apellidos", "Aula", "Correo"))
    if not result:
        result="No encontrado..."
    else:
        for index,x in enumerate(result):
            num=0
            index+=3
            id_reference=str(x[0])

            for y in x:
                l_mostrar=Label(panel2_admin, text=y,bg=QuesColor,font=("Bahnschrift Condensed",13))
                l_mostrar.grid(row=index, column=num, padx=(50,0))
                num+=1
            l.append(id_reference)
    csv_btn=Button(panel2_admin, text="Guardar en un CSV",command = lambda: write_to_csv(result))        
    csv_btn.grid(row=0,column=0,pady=10,padx=(10,0),ipadx=10)
    
    excel_btn=Button(panel2_admin, text="Guardar en un Excel",command = lambda: write_to_excel(result))        
    excel_btn.grid(row=1,column=0,pady=10,padx=(10,0),ipadx=6)
    
    button_dict_editar={}
    button_dict_eliminar={}
    for e in range(1,len(l)-1):
        def func_editar(x=l[e]):
            return editar_ahora(x)
        def func_eliminar(x=l[e]):
            return eliminar_ahora(x)
        def func_editar_last():
            return editar_ahora(l[-1])
        def func_eliminar_last():
            return eliminar_ahora(l[-1])
         
        button_dict_editar[e]=Button(panel2_admin, text="Editar", command = func_editar)
        button_dict_editar[e].grid(row = e+3, column = 5, padx = (10,0), pady = 5) 
        button_dict_eliminar[e]=Button(panel2_admin, text="Eliminar", command =func_eliminar)
        button_dict_eliminar[e].grid(row = e+3, column = 6, padx = (10,0), pady = 5)
    if len(l)>2:
        button_dict_editar[l[-1]]=Button(panel2_admin, text="Editar", command = func_editar_last)
        button_dict_editar[l[-1]].grid(row = len(l)+2, column = 5, padx = (10,0), pady = 5) 
        button_dict_eliminar[l[-1]]=Button(panel2_admin, text="Eliminar", command =func_eliminar_last)
        button_dict_eliminar[l[-1]].grid(row = len(l)+2, column = 6, padx = (10,0), pady = 5)
    
    if len(result)==2:
        def func_editar_only():
            editar_ahora(result[1][0])
        def func_eliminar_only():
            eliminar_ahora(result[1][0])
            
        button_dict_editar_only=Button(panel2_admin, text="Editar", command = func_editar_only)
        button_dict_editar_only.grid(row = 4, column = 5, padx = (10,0), pady = 5) 
        button_dict_eliminar_only=Button(panel2_admin, text="Eliminar", command =func_eliminar_only)
        button_dict_eliminar_only.grid(row = 4, column = 6, padx = (10,0), pady = 5)  
    
    
    
    
    
    
def listar_student():
    
    clear_panel2()
    global querylabel
    clock(panel2_admin,1100,20)
    con=sqlite3.connect('Escuela.db')    #Create a database or connect to one
    c= con.cursor()                     #Create cursor
    c.execute("SELECT * FROM Estudiantes")
    registros=c.fetchall()
    
    # l_nombre_columnas=Label(panel2_admin, text="ID")
    # l_nombre_columnas.grid(row=0, column=0, padx=(10,0))
    registros.insert(0,("ID","Nombre y Apellidos", "Aula", "Correo"))
    
    csv_btn=Button(panel2_admin, text="Guardar en un CSV",command = lambda: write_to_csv(registros))        
    csv_btn.grid(row=0,column=0,pady=10,padx=(10,0),ipadx=10)
    
    excel_btn=Button(panel2_admin, text="Guardar en un Excel",command = lambda: write_to_excel(registros))        
    excel_btn.grid(row=1,column=0,pady=10,padx=(10,0),ipadx=6)
    global buscar_btn_combo
    buscar_btn_combo=ttk.Combobox(panel2_admin, values=["Buscar por...","Nombre y Apellidos","Aula","Correo"]) 
    buscar_btn_combo.current(0)       
    buscar_btn_combo.grid(row=0,column=1,pady=10,padx=(15,0),ipadx=6)
    global f_busqueda
    f_busqueda=Entry(panel2_admin)
    f_busqueda.grid(row=0,column=2,pady=10,padx=8)
    global buscar_btn
    buscar_btn=Button(panel2_admin,text="Buscar",command=buscar_ahora)
    buscar_btn.grid(row=0,column=3,pady=10,padx=8)
    l=[]
    for index,x in enumerate(registros):
        #num=1
        num=0
        index+=2
        
        for y in x:
            #mostrar_frame=Frame(panel2_admin)
            id_reference=str(x[0])
            
            l_mostrar=Label(panel2_admin, text=y,bg=QuesColor,font=("Bahnschrift Condensed",13))
            l_mostrar.grid(row=index, column=num, padx=(50,0))
            # if index!=1:
            #     edit_button=Button(panel2_admin, text="Editar", command=lambda:editar_ahora())
            #     edit_button.grid(row = index, column = 5, padx = (10,0), pady = 5)       
            #     delete_button=Button(panel2_admin, text="Eliminar", command =lambda: eliminar_ahora(id_reference,index))
            #     delete_button.grid(row = index, column = 6, padx = (10,0), pady = 5)
            num+=1
        l.append(id_reference)
        #a=l[1:]     
    button_dict_editar={}
    button_dict_eliminar={}
    for e in range(1,len(l)-1):
        def func_editar(x=l[e]):
            return editar_ahora(x)
        def func_eliminar(x=l[e]):
            return eliminar_ahora(x)
        def func_editar_last():
            return editar_ahora(l[-1])
        def func_eliminar_last():
            return eliminar_ahora(l[-1])
         
        button_dict_editar[e]=Button(panel2_admin, text="Editar", command = func_editar)
        button_dict_editar[e].grid(row = e+2, column = 5, padx = (10,0), pady = 5) 
        button_dict_eliminar[e]=Button(panel2_admin, text="Eliminar", command =func_eliminar)
        button_dict_eliminar[e].grid(row = e+2, column = 6, padx = (10,0), pady = 5)
    if len(l)>2:
        button_dict_editar[l[-1]]=Button(panel2_admin, text="Editar", command = func_editar_last)
        button_dict_editar[l[-1]].grid(row = len(l)+1, column = 5, padx = (10,0), pady = 5) 
        button_dict_eliminar[l[-1]]=Button(panel2_admin, text="Eliminar", command =func_eliminar_last)
        button_dict_eliminar[l[-1]].grid(row = len(l)+1, column = 6, padx = (10,0), pady = 5)
    #print(len(registros))
    if len(registros)==2:
        def func_editar_only():
            editar_ahora(registros[1][0])
        def func_eliminar_only():
            eliminar_ahora(registros[1][0])
            
        button_dict_editar_only=Button(panel2_admin, text="Editar", command = func_editar_only)
        button_dict_editar_only.grid(row = 3, column = 5, padx = (10,0), pady = 5) 
        button_dict_eliminar_only=Button(panel2_admin, text="Eliminar", command =func_eliminar_only)
        button_dict_eliminar_only.grid(row = 3, column = 6, padx = (10,0), pady = 5)  
    
    #print(l)
    con.commit()
    c.close()


def modulos(valor):
    # for widget in panel2_admin.winfo_children():
    #         widget.destroy()
    clock(panel2_admin,x=1100,y=20)
    pass
    
def estudiantes(valor):
    clear_panel2()

    target_student_options=mylistbox_admin2.get(ANCHOR)
    print(target_student_options)
    if target_student_options=="Añadir Estudiante":
        label_nombre_completo_estudiante=Label(panel2_admin,text="Nombre Completo",bg=QuesColor)
        label_nombre_completo_estudiante.grid(column=0,row=0)
        global f_nombre_completo
        f_nombre_completo=Entry(panel2_admin)
        f_nombre_completo.grid(column=1,row=0)
        
        label_aula_estudiante=Label(panel2_admin,text="Aula del estudiante",bg=QuesColor)
        label_aula_estudiante.grid(column=0,row=1)
        global f_aula
        f_aula=Entry(panel2_admin)
        f_aula.grid(column=1,row=1)
        
        label_correo_estudiante=Label(panel2_admin,text="Correo del estudiante",bg=QuesColor)
        label_correo_estudiante.grid(column=0,row=2)
        global f_correo
        f_correo=Entry(panel2_admin)
        f_correo.grid(column=1,row=2)
        
        submit_btn_estudiante=Button(panel2_admin,text="Agregar",command=submit_estudiante)
        submit_btn_estudiante.grid(column=1,row=4)
    elif target_student_options=="Listar Estudiantes":
        listar_student()
    clock(panel2_admin,x=1100,y=20)
def go(event):
    hide_all_frames_questions()
    clock(panel2,820,20)
    cs=mylistbox.get(ANCHOR)
    fil=30
    # global valor
    #valor=0
    global varOpcion
    varOpcion=StringVar()
    for key,items in Temas[cs].items():
        a= " ".join(items)
        # bottom.config(text=key)
        # bottom.place(x=50,y=fil)
        bot_label=Label(panel2,text=key,bg=QuesColor)
        bot_label.place(x=50,y=fil)                    #funciona
        for i in items:
            varOpcion.set(items[0])
            # bottom.config(text=key)
            # bottom.place(x=50,y=fil)
            #varOpcion.set(items[0])
            a=Radiobutton(panel2,text=i,variable=varOpcion,value=i,bg=QuesColor)
            a.place(x=50,y=fil+20)
            fil+=20
            # valor+=1
        #valor=0
        fil+=50
    
    global enviar
    enviar=Button(panel2,text="Enviar",bg="dark slate gray",fg="white",cursor="hand2")
    enviar.place(x=200,y=fil+20)  
    

root=Tk()
#root.resizable(0,0)
Temas={'Banco de preguntas Seguridad y Salud del Trabajo':{"1.Para garantizar la protección contra el contacto directo con la corriente eléctrica se utilizan:":["Desconexión automática de la red",
"Colocación al alcance del hombre",
"Emplazamientos no conductores",
"Barreras o envolventes"],"2.Para garantizar la protección contra el contacto directo con la corriente eléctrica se utilizan:":["2Desconexión automática de la red",
"Colocación al alcance del hombre",
"2Emplazamientos no conductores",
"Barreras o envolventes"],"3.Para garantizar la protección contra el contacto directo con la corriente eléctrica se utilizan:":["3Desconexión automática de la red",
"Colocación al alcance del hombre",
"3Emplazamientos no conductores",
"Barreras o envolventes"]},
       'Electricidad':{"2.Para garantizar la protección contra el contacto directo con la corriente eléctrica se utilizan:":["2Desconexión automática de la red",
"Colocación al alcance del hombre",
"2Emplazamientos no conductores",
"Barreras o envolventes"]},
       'Equipos de Subestaciones':{},
       'Fundamentos de Operación':{},
       'Fundamentos de Operaciones II':{},
       'Generadores de CA':{},
       'Mediciones Eléctricas':{},
       'Preguntas de  RS 136':{},
       'Preguntas de Electricidad':{},
       'Preguntas de Equipos de SE ':{},
       'Preguntas de Equipos de Subestaciones':{},
       'Preguntas de Generadores de CA':{},
       'Preguntas de Mediciones Eléctricas':{},
       'Preguntas de Protecciones':{},
       'Preguntas de SI':{},
       'Preguntas int de planos':{},
       'Preguntas Protecciones Electricas':{},
       'Protecciones Eléctricas':{},
       'Seguridad Industrial':{}
}


root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")


QuesColor="SlateGray1"
ModuleColor="LightSkyBlue3"


def hide_all_frames():
        #Loop thru and destroy all children in previus frames
        for widget in RightFrame.winfo_children():
            widget.destroy()
            
        for widget in l_frame_user_auth.winfo_children():
            widget.destroy()
        RightFrame.pack_forget()
        l_frame_user_auth.pack_forget()

def hide_all_frames_questions():
        #Loop thru and destroy all children in previus frames
        for widget in panel2.winfo_children():
            widget.destroy()
            

        panel2.pack_forget()
        
def validate_password(teacher_or_admin):        
    if teacher_or_admin==1 and e_user.get()=="a":              #"A6m1n15t8a608" clave seleccionada pero para ahorrar tiempo trabajare con a
        is_admin()
        
    elif teacher_or_admin==2 and e_user.get()=="Teacher":               # bd con profesores?
        return
    else:
        messagebox.showerror("Clave incorrecta", "Introduzca nuevamente su contraseña")
        if teacher_or_admin==1:
            admin_auth()
        else:
            teacher_auth()
def admin_auth():
   
    e_user.delete(0,END)
    l_user.config(text="Password")
    e_user.config(show="*")
    check_user_btn.config(command=lambda:validate_password(1))



def teacher_auth():
    e_user.delete(0,END)
    l_user.config(text="Password")
    e_user.config(show="*")
    check_user_btn.config(command=lambda:validate_password(2))

    
    
    
def student_auth():
    if e_user.get()=="Admin":
        admin_auth()
        return
    elif e_user.get()=="Profesor":
        teacher_auth()
        return
    hide_all_frames()
    
    
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    root.geometry("{}x{}".format(width,height))
    panel1=PanedWindow(bd=4,relief="raised",bg=ModuleColor)
    panel1.pack(fill=BOTH,expand=1)




    #Creando frame y scrollbar
    my_frame=Frame(panel1,bg=ModuleColor)
    global mylistbox
    my_scrollbar=Scrollbar(my_frame,orient=VERTICAL)
    mylistbox=Listbox(my_frame,width=50,yscrollcommand=my_scrollbar.set,height=100,bg="dark slate gray",fg="white",cursor="hand2",font=("Bahnschrift Condensed",14))
    my_scrollbar.config(command=mylistbox.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    my_scrollbar.config(command=mylistbox.yview)
    my_scrollbar.pack(side=RIGHT,fill=Y)
    indice=Label(my_frame,text="Índice:",bg=ModuleColor,font=("Bahnschrift Condensed",14))
    indice.pack(pady=10)
    mylistbox.bind("<Double-1>",go)
    mylistbox.pack(pady=5)
    my_frame.pack()


    panel1.add(my_frame)

    mylistbox.pack()
    for i in Temas.keys():
        mylistbox.insert(END,i)



    #Creando segundo panel
    global panel2
    panel2=PanedWindow(panel1,orient=VERTICAL,bd=4,relief="raised",bg=QuesColor)
    panel1.add(panel2)

    
    
    clock(panel2,820,20)




con=sqlite3.connect('Escuela.db')  #Create a database or connect to one

c= con.cursor()            #Create cursor


c.execute("CREATE TABLE IF NOT EXISTS Estudiantes(\
    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
    nombre_completo VARCHAR(255),\
    aula VARCHAR(10),\
    correo VARCHAR(100))")

def login():
    root.geometry("500x500")
    global l_frame_user_auth
    l_frame_user_auth=LabelFrame(root,width=275,height=350,background=ModuleColor,bd=3,font=("Bahnschrift Condensed",12))
    l_frame_user_auth.pack(side=LEFT,fill=Y)

    #anchoFLeft=500-l_frame_user_auth.__getitem__("width")
    global RightFrame
    RightFrame=LabelFrame(root,width=225,height=700,background=QuesColor,text="Ingreso",bd=3,font=("Bahnschrift Condensed",12))
    RightFrame.pack(side=RIGHT,fill=BOTH,expand=1)

    global l_user
    l_user=Label(RightFrame,text="Nombre",bg=QuesColor)
    l_user.pack(pady=(80,0))

    global e_user
    # e_user=Entry(RightFrame)
    # e_user.pack()
    con=sqlite3.connect('Escuela.db')    #Create a database or connect to one
    c= con.cursor()                     #Create cursor
    c.execute("SELECT nombre_completo FROM Estudiantes")
    registros=c.fetchall()
    print_records=[]
    for registro in registros:
        print_records.append(str(registro[0]))
    print_records.sort()
    e_user=ttk.Combobox(RightFrame, values=print_records)
    e_user.pack()
    
    global check_user_btn
    check_user_btn=Button(RightFrame,text="Submit",command=student_auth,bg=QuesColor,cursor="hand2")
    check_user_btn.pack(pady=20)

login()


def is_admin():
    hide_all_frames()
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    #root.geometry("{}x{}".format(width,height))
    root.geometry("%dx%d" % (width, height))
    Panel_admin_left=PanedWindow(bd=4,relief="raised",bg=ModuleColor)
    Panel_admin_left.pack(fill=BOTH,expand=1)
    
    # #Creando frame y scrollbar
    my_frame_admin1=Frame(Panel_admin_left,bg=ModuleColor,height=60)
    indice=Label(my_frame_admin1,text="Acciones:",bg=ModuleColor,font=("Bahnschrift Condensed",14))
    indice.pack(pady=5)
    
    # panelprueba1=PanedWindow(my_frame_admin1,bd=4,relief="raised",bg=ModuleColor)
    # panelprueba1.pack(fill=BOTH,expand=YES)
    
    panel_1=Frame(my_frame_admin1,bg=ModuleColor)
    panel_1.pack(fill=BOTH,expand=YES,pady=(60,0))
    s1=Label(panel_1,text="Tabla Módulos",bg=ModuleColor,font=("Bahnschrift Condensed",14)).pack()
    panel_2=Frame(my_frame_admin1,bg=ModuleColor)
    panel_2.pack(fill=BOTH,expand=YES,pady=60)
    s2=Label(panel_2,text="Tabla Estudiantes",bg=ModuleColor,font=("Bahnschrift Condensed",14)).pack()
    
    #Validar si es profesor o admin
    # panel_3=Frame(my_frame_admin1,bg=ModuleColor)
    # panel_3.pack(fill=BOTH,expand=YES)
    # s3=Label(panel_3,text="Tabla Profesores",bg=ModuleColor,font=("Bahnschrift Condensed",14)).pack()        #Próxima versión
    
    global mylistbox_admin
    #my_scrollbar_admin=Scrollbar(panel_1,orient=VERTICAL)
    # Agregar a linea siguiente ,yscrollcommand=my_scrollbar_admin.set si se desea scroll bar
    mylistbox_admin=Listbox(panel_1,width=20,justify=CENTER,height=0,bg="dark slate gray",fg="white",cursor="hand2",font=("Bahnschrift Condensed",14))
    #my_scrollbar_admin.config(command=mylistbox_admin.yview)
    #my_scrollbar_admin.pack(side=RIGHT,fill=Y)
    # indice=Label(my_frame_admin2,text="Acciones",bg=ModuleColor,font=("Bahnschrift Condensed",14))
    # indice.pack(pady=10)
    mylistbox_admin.bind("<Double-1>",modulos)
    mylistbox_admin.pack()
    
    listbox_main1=["Añadir Módulo","Mostrar Módulos"]
    for elements in listbox_main1:
        mylistbox_admin.insert(END,elements)

    global mylistbox_admin2
    #my_scrollbar_admin2=Scrollbar(panel_2,orient=VERTICAL)
    mylistbox_admin2=Listbox(panel_2,width=20,justify=CENTER,height=0,bg="dark slate gray",fg="white",cursor="hand2",font=("Bahnschrift Condensed",14))
    #my_scrollbar_admin2.config(command=mylistbox_admin2.yview)
    #my_scrollbar_admin2.pack(side=RIGHT,fill=Y)
    # indice=Label(my_frame_admin2,text="Acciones",bg=ModuleColor,font=("Bahnschrift Condensed",14))
    # indice.pack(pady=10)
    mylistbox_admin2.bind("<Double-1>",estudiantes)
    mylistbox_admin2.pack()
    
    
    listbox_main2=["Añadir Estudiante","Listar Estudiantes"]
    for elements in listbox_main2:
        mylistbox_admin2.insert(END,elements)
####################################################################################################################
    # Tabla profesores. Se va a desarrollar en próximas versiones
    
    # global mylistbox_admin3
    # my_scrollbar_admin3=Scrollbar(panel_3,orient=VERTICAL)
    # mylistbox_admin3=Listbox(panel_3,width=50,yscrollcommand=my_scrollbar_admin3.set,bg="dark slate gray",fg="white",cursor="hand2",font=("Bahnschrift Condensed",14))
    # my_scrollbar_admin3.config(command=mylistbox_admin3.yview)
    # my_scrollbar_admin3.pack(side=RIGHT,fill=Y)
    # # indice=Label(my_frame_admin2,text="Acciones",bg=ModuleColor,font=("Bahnschrift Condensed",14))
    # # indice.pack(pady=10)
    # mylistbox_admin3.bind("<Double-1>",go)
    # mylistbox_admin3.pack()

####################################################################################################################


    my_frame_admin1.pack(ipadx=10)
    Panel_admin_left.add(my_frame_admin1)


    

    #Creando segundo panel
    global panel2_admin
    panel2_admin=PanedWindow(Panel_admin_left,orient=VERTICAL,bd=4,relief="raised",bg=QuesColor)
    Panel_admin_left.add(panel2_admin)

    
    clock(panel2_admin,1100,20)

     

con.commit()
c.close()

root.mainloop()



