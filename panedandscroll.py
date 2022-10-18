from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import time

def clock():
    my_time=Label(panel2,text="",bg="white",font=("Bahnschrift Condensed",13),fg="dark slate gray",bd=4,relief="groove",width=10)
    my_time.place(x=820,y=20)
    hour=time.strftime("%I")            #H para darla en forato 24h, I formato 12 horas
    minute=time.strftime("%M")
    second=time.strftime("%S")
    am_pm=time.strftime("%p")
    my_time.config(text=hour+":"+minute+":"+second+" "+am_pm)
    my_time.after(1000,clock)
    



def go(event):
    hide_all_frames_questions()
    clock()
    

    cs=mylistbox.get(ANCHOR)
    
     
    fil=30
    valor=0
    global varOpcion
    varOpcion=StringVar()
    for key,items in Temas[cs].items():
        a= " ".join(items)
        # bottom.config(text=key)
        # bottom.place(x=50,y=fil)
        bot_label=Label(panel2,text=key,bg=QuesColor)
        bot_label.place(x=50,y=fil)                    #funciona
        varOpcion.set(items[0])
        for i in items:
            
            # bottom.config(text=key)
            # bottom.place(x=50,y=fil)
            #varOpcion.set(items[0])
            a=Radiobutton(panel2,text=i,variable=varOpcion,value=valor,bg=QuesColor)
            a.place(x=50,y=fil+20)
            fil+=20
            valor+=1
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

    
    
    clock()




con=sqlite3.connect('Escuela.db')  #Create a database or connect to one

c= con.cursor()            #Create cursor


c.execute("CREATE TABLE IF NOT EXISTS Escuela(\
    user_id INT AUTO_INCREMENT PRIMARY KEY,\
    nombre VARCHAR(255),\
    primer_apellido VARCHAR(255),\
    segundo_apellido VARCHAR(255))")

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
    e_user=Entry(RightFrame)
    e_user.pack()

    global check_user_btn
    check_user_btn=Button(RightFrame,text="Submit",command=student_auth,bg=QuesColor,cursor="hand2")
    check_user_btn.pack(pady=20)

login()


def is_admin():
    hide_all_frames()
    width=root.winfo_screenwidth()
    height=root.winfo_screenheight()
    root.geometry("{}x{}".format(width,height))
    Panel_admin_left=PanedWindow(bd=4,relief="raised",bg=ModuleColor)
    Panel_admin_left.pack(fill=BOTH,expand=1)
    
    # #Creando frame y scrollbar
    my_frame_admin1=Frame(Panel_admin_left,bg=ModuleColor,height=60)
    indice=Label(my_frame_admin1,text="Acciones:",bg=ModuleColor,font=("Bahnschrift Condensed",14))
    indice.pack(pady=5)
    
    # panelprueba1=PanedWindow(my_frame_admin1,bd=4,relief="raised",bg=ModuleColor)
    # panelprueba1.pack(fill=BOTH,expand=YES)
    
    panel_1=Frame(my_frame_admin1,bg=ModuleColor)
    panel_1.pack(fill=BOTH,expand=YES)
    #s1=Label(panel_1,text="Soy panel 1").pack()
    panel_2=Frame(my_frame_admin1,bg=ModuleColor)
    panel_2.pack(fill=BOTH,expand=YES,pady=20)
    #s2=Label(panel_2,text="Soy panel 2").pack()
    
    #Validar si es profesor o admin
    panel_3=Frame(my_frame_admin1,bg=ModuleColor)
    panel_3.pack(fill=BOTH,expand=YES)
   # s2=Label(panel_3,text="Soy panel 3").pack()
    
    global mylistbox_admin
    my_scrollbar_admin=Scrollbar(panel_1,orient=VERTICAL)
    mylistbox_admin=Listbox(panel_1,width=50,yscrollcommand=my_scrollbar_admin.set,bg="dark slate gray",fg="white",cursor="hand2",font=("Bahnschrift Condensed",14))
    my_scrollbar_admin.config(command=mylistbox_admin.yview)
    my_scrollbar_admin.pack(side=RIGHT,fill=Y)
    # indice=Label(my_frame_admin2,text="Acciones",bg=ModuleColor,font=("Bahnschrift Condensed",14))
    # indice.pack(pady=10)
    mylistbox_admin.bind("<Double-1>",go)
    mylistbox_admin.pack()
    


    global mylistbox_admin2
    my_scrollbar_admin2=Scrollbar(panel_2,orient=VERTICAL)
    mylistbox_admin2=Listbox(panel_2,width=50,yscrollcommand=my_scrollbar_admin2.set,bg="dark slate gray",fg="white",cursor="hand2",font=("Bahnschrift Condensed",14))
    my_scrollbar_admin2.config(command=mylistbox_admin2.yview)
    my_scrollbar_admin2.pack(side=RIGHT,fill=Y)
    # indice=Label(my_frame_admin2,text="Acciones",bg=ModuleColor,font=("Bahnschrift Condensed",14))
    # indice.pack(pady=10)
    mylistbox_admin2.bind("<Double-1>",go)
    mylistbox_admin2.pack()
    


    global mylistbox_admin3
    my_scrollbar_admin3=Scrollbar(panel_3,orient=VERTICAL)
    mylistbox_admin3=Listbox(panel_3,width=50,yscrollcommand=my_scrollbar_admin3.set,bg="dark slate gray",fg="white",cursor="hand2",font=("Bahnschrift Condensed",14))
    my_scrollbar_admin3.config(command=mylistbox_admin3.yview)
    my_scrollbar_admin3.pack(side=RIGHT,fill=Y)
    # indice=Label(my_frame_admin2,text="Acciones",bg=ModuleColor,font=("Bahnschrift Condensed",14))
    # indice.pack(pady=10)
    mylistbox_admin3.bind("<Double-1>",go)
    mylistbox_admin3.pack()




    my_frame_admin1.pack(ipadx=10)
    Panel_admin_left.add(my_frame_admin1)


    

    #Creando segundo panel
    global panel2
    panel2=PanedWindow(Panel_admin_left,orient=VERTICAL,bd=4,relief="raised",bg=QuesColor)
    Panel_admin_left.add(panel2)

    
    clock()

     

con.commit()
c.close()

root.mainloop()