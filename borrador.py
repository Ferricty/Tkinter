from tkinter import *

from matplotlib.pyplot import fill


def go(event):
    #cs=mylistbox.curselection()
    cs=mylistbox.get(ANCHOR)
    panel2.add(bottom)
    listas = [] 
    # for key in Temas.keys(): 
    #     listas.append(key) 
    #print(mylistbox.get(cs))        
    print(cs)
    
    for key,items in Temas[cs].items():
        a= " ".join(items)
        bottom.config(text=key+"\n"+a)



root=Tk()

Temas={'Banco  de preguntas Seguridad y Salud del Trabajo':{"1.Para garantizar la protección contra el contacto directo con la corriente eléctrica se utilizan:":["Desconexión automática de la red",
"Colocación al alcance del hombre",
"Emplazamientos no conductores",
"Barreras o envolventes"]},
       'Electricidad':{},
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
width=root.winfo_screenwidth()
height=root.winfo_screenheight()
root.geometry("{}x{}".format(width,height))



panel1=PanedWindow(bd=4,relief="raised",bg="red")
panel1.pack(fill=BOTH,expand=1)




#Creando frame y scrollbar
my_frame=Frame(panel1)

my_scrollbar=Scrollbar(my_frame,orient=VERTICAL)
mylistbox=Listbox(my_frame,width=50,yscrollcommand=my_scrollbar.set,height=100)
my_scrollbar.config(command=mylistbox.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
my_scrollbar.config(command=mylistbox.yview)
my_scrollbar.pack(side=RIGHT,fill=Y)
indice=Label(my_frame,text="Indice:")
indice.pack(pady=10)
mylistbox.bind("<Double-1>",go)
mylistbox.pack(pady=5)
my_frame.pack()


panel1.add(my_frame)

mylistbox.pack()
for i in Temas.keys():
    mylistbox.insert(END,i)



#Creando segundo panel
panel2=PanedWindow(panel1,orient=VERTICAL,bd=4,relief="raised",bg="blue")
panel1.add(panel2)
# top=Label(panel2,text="Top Panel")
# panel2.add(top)
bottom=Label(panel2,text="")





root.mainloop()