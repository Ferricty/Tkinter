
from tkinter import *

root=Tk()
root.title("Calculadora")

miframe=Frame(root)    
miframe.pack()

numeropantalla=StringVar()
operacion=""
resultado=0


pantalla=Entry(miframe,textvariable=numeropantalla)
pantalla.grid(row=1,column=1,padx=10,pady=10, columnspan=4)
pantalla.config(bg="black",fg="#03f943",justify="right")

def button_clic(num):
    global operacion
    if operacion!="":
        numeropantalla.set(num)
    else:
        numeropantalla.set(numeropantalla.get()+num)
    
def suma(num):
    global operacion
    global resultado
    resultado+=int(num)
    operacion="suma"
    numeropantalla.set(resultado)
    
    
def igual():
    global resultado
    numeropantalla.set(resultado+int(numeropantalla.get()))
    resultado=0

button1=Button(miframe,text="1",width=3,command=lambda:button_clic("1"))
button2=Button(miframe,text="2",width=3,command=lambda:button_clic("2"))
button3=Button(miframe,text="3",width=3,command=lambda:button_clic("3"))
button4=Button(miframe,text="4",width=3,command=lambda:button_clic("4"))
button5=Button(miframe,text="5",width=3,command=lambda:button_clic("5"))
button6=Button(miframe,text="6",width=3,command=lambda:button_clic("6"))
button7=Button(miframe,text="7",width=3,command=lambda:button_clic("7"))
button8=Button(miframe,text="8",width=3,command=lambda:button_clic("8"))
button9=Button(miframe,text="9",width=3,command=lambda:button_clic("9"))
button0=Button(miframe,text="0",width=3,command=lambda:button_clic("0"))

button_suma=Button(miframe,text="+",width=3,command=lambda:suma(numeropantalla.get()))
button_resta=Button(miframe,text="-",width=3)
button_multiplicar=Button(miframe,text="*",width=3)
button_dividir=Button(miframe,text="/",width=3)
#button_clear=Button(miframe,text="C",width=3)
button_igual=Button(miframe,text="=",width=3,command=lambda:igual())
button_coma=Button(miframe,text=",",width=3,command=lambda:button_clic("."))


button0.grid(row=5,column=1)

#button_clear.grid(row=4,column=1)
button_igual.grid(row=5,column=3)
button_coma.grid(row=5,column=2)
button_suma.grid(row=5,column=4)

button1.grid(row=4,column=1)
button2.grid(row=4,column=2)
button3.grid(row=4,column=3)
button_resta.grid(row=4,column=4)

button4.grid(row=3,column=1)
button5.grid(row=3,column=2)
button6.grid(row=3,column=3)
button_multiplicar.grid(row=3,column=4)

button7.grid(row=2,column=1)
button8.grid(row=2,column=2)
button9.grid(row=2,column=3)
button_dividir.grid(row=2,column=4)


root.mainloop()


