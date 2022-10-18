
from tkinter import *

'''

math-> indica la operacion que se esta realizando sumar,restar,multiplicar,dividir,
       nada(andas aburrido dando igual a ver que pasa)
       
estado-> 0 se ha pulsado clear o es la primera operacion
      -> 1 se ejecuto una operacion anteriormente
      -> 2 se ha colocado , anteriormente  

queda pendiente:
-realizar la operacion anterior al pulsar igual
-mejorar ui
-agregar mas funcionalidades a la calculadora
-guardar las ultimas operaciones

'''
resultado=0
f_num=0
estado=0  
l=[]
math="nada"
root=Tk()
root.title("Calculadora")

e= Entry(root,width=20,border="3px")
e.grid(row=0,column=0,columnspan=4,padx=10,pady=10)
e.config(background="black",fg="#03f943",justify='right')


def button_clic(number):
    global estado
    global math
    
    
    if estado==1:
        e.delete(0,END)
        estado=0
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))
    

def button_add():
    global estado
    global f_num

    if estado==1:
        first_number=resultado
    else:
        first_number=e.get()

    f_num=float(first_number)
    global math
    math="addition"
    
    e.delete(0,END)

def button_mult():
    global estado
    global f_num
    
    if estado==1:
        first_number=resultado
    else:
        first_number=e.get()
    f_num=float(first_number)
    
    global math
    math="product"
    
    e.delete(0,END)

def button_rest():
    global estado
    global f_num
    
    
    
    if estado==1:
        first_number=resultado
    else:
        first_number=e.get()
    f_num=float(first_number)
    
    global math
    math="substract"
    
    e.delete(0,END)

def button_divid():
    global estado
    global f_num
    
    if estado==1:
        first_number=resultado
    else:
        first_number=e.get()
    f_num=float(first_number)
    
    global math
    math="dividir"
    
    e.delete(0,END)


def button_clr():
    e.delete(0,END)
    global estado
    global math
    estado=0
    math="nada"
 
    
def button_equal():
    global estado
    global f_num
    global resultado
    global l
    
    second_number=e.get()
    #l.insert(0,resultado)
    #l.insert(1,second_number)
    # print(l)
    e.delete(0,END)
    # if resultado!=0:
    #     f_num=float(l[-1])
        
        
    if math=="nada":
        resultado=float(second_number)
        f_num=e.insert(0,resultado)
        estado=1
        
    if math=="addition":
        resultado=f_num + float(second_number)
        f_num=e.insert(0,resultado)
        estado=1
        
    if math=="product":
        resultado=f_num * float(second_number)
        f_num=e.insert(0,resultado)
        estado=1
        
    if math=="substract":
        resultado=f_num - float(second_number)
        f_num=e.insert(0,resultado)
        estado=1
        
    if math=="dividir":
        resultado=f_num / float(second_number)
        f_num=e.insert(0,resultado)
        estado=1


def button_dot():
    global estado
    if estado==2:
        return
    current=e.get()
    e.delete(0,END)
    estado=2
    e.insert(0,str(current)+".")
    


button1=Button(root,text="1",padx=10,pady=10,command=lambda:button_clic(1))
button2=Button(root,text="2",padx=10,pady=10,command=lambda:button_clic(2))
button3=Button(root,text="3",padx=10,pady=10,command=lambda:button_clic(3))
button4=Button(root,text="4",padx=10,pady=10,command=lambda:button_clic(4))
button5=Button(root,text="5",padx=10,pady=10,command=lambda:button_clic(5))
button6=Button(root,text="6",padx=10,pady=10,command=lambda:button_clic(6))
button7=Button(root,text="7",padx=10,pady=10,command=lambda:button_clic(7))
button8=Button(root,text="8",padx=10,pady=10,command=lambda:button_clic(8))
button9=Button(root,text="9",padx=10,pady=10,command=lambda:button_clic(9))
button0=Button(root,text="0",padx=10,pady=10,command=lambda:button_clic(0))
button_suma=Button(root,text="+",padx=10,pady=10,command=lambda:button_add())
button_resta=Button(root,text="-",padx=10,pady=10,command=lambda:button_rest())
button_multiplicar=Button(root,text="*",padx=10,pady=10,command=lambda:button_mult())
button_dividir=Button(root,text="/",padx=10,pady=10,command=lambda:button_divid())
button_clear=Button(root,text="C",padx=10,pady=10,command=button_clr)
button_igual=Button(root,text="=",padx=10,pady=10,command=button_equal)
button_coma=Button(root,text=",",padx=10,pady=10,state=NORMAL,command=button_dot)


button0.grid(row=4,column=2)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)


button_suma.grid(row=3,column=3)
button_resta.grid(row=2,column=3)
button_multiplicar.grid(row=1,column=3)
button_dividir.grid(row=4,column=3)
button_clear.grid(row=4,column=1)
button_igual.grid(row=4,column=0)
button_coma.grid(row=4,column=4)




root.mainloop()


