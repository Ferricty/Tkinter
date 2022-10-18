from tkinter import *

raiz=Tk()       #Construye la ventana

raiz.title("Nombre")    #Establece Titulo de la ventana

raiz.iconbitmap("bruja.ico")    #Icono de la ventana

#raiz.resizable(0,0)    #Impide que se pueda alterar dimensiones de la ventana. (ancho, alto)
                       #Poniendo en 1 uno de ellos se puede redimensionar la ventana ya sea alto ancho o ambas

raiz.geometry("600x500")        #Establece tamaño para la ventana

raiz.config(bg="#AAAAAA")

miframe=Frame()         #Creacion de frame

miframe.pack(padx=10,pady=50)   #Separacion de los bordes con respecto a la raiz

#variable=Label(contenedor, opciones )          son las mismas opciones para Entry

'''
text        texto que se uestra en el label
anchor      controla posicion del texto si hay espacio suficiente para el. center por defecto
bg          color de fondo
bitmap      mapa de bits que se mostrara como grafico
bd          grosor del borde 2px por defecto
font        fuente a mostrar
fg          color de fuente
width       ancho en caracteres
height      alto en caracteres
image       muestra imagen en lugar de texto
justify     justificacion del texto

'''
#primertexto=Label(miframe, text="hola",fg="blue",bg="red",font=("Times New Roman",18))
#primertexto.place(x=100,y=100)                      #establece posicion del label dentro del frame

primertexto=Label(miframe, text="Nombre: ").place(x=100,y=100)
dataentry=Entry(miframe).place(x=150,y=100)


miframe.config(bg="white", width=500, height=400)     #color de fondo del frame y dimensiones del mismo

raiz.mainloop()     #Ejecuta ciclo infinito para mantener la ventana. Debe ir al final del codigo