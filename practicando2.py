from tkinter import *

raiz=Tk()

raiz.title("Plantilla")

principal=Frame(raiz,width=500,height=600)
principal.pack()

minombre=StringVar()

nombre=Label(principal,text="Nombre")
nombre.grid(column=0,row=0,padx=10,pady=10,sticky="e")
nombre1=Entry(principal, textvariable=minombre)
nombre1.grid(column=1,row=0,padx=10,pady=10)

passw=Label(principal,text="Password")
passw.grid(column=0,row=1,padx=10,pady=10,sticky="e")
passw1=Entry(principal)
passw1.grid(column=1,row=1,padx=10,pady=10)
passw1.config(show="*")

direccion=Label(principal,text="Direccion")
direccion.grid(column=0,row=3,padx=10,pady=10,sticky="e")
direccion1=Entry(principal)
direccion1.grid(column=1,row=3,padx=10,pady=10)

comentario=Label(principal,text="Comentario")
comentario.grid(column=0,row=4,padx=10,pady=10,sticky="e")
comentario1=Text(principal, height=4,width=15)
comentario1.grid(column=1,row=4,padx=10,pady=10)

scrollver=Scrollbar(principal,command=comentario1.yview)        #a;adiendo barra de desplazamiento vertical al textareay
scrollver.grid(column=2,row=4,sticky="nsew")
comentario1.config(yscrollcommand=scrollver.set)

def enviar():
    minombre.set("Frank")

botonenviar=Button(raiz,text="Enviar", command=enviar)
botonenviar.pack()

raiz.mainloop()