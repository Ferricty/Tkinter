#Text to speech
from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")

#Cargando imagen
img=Image.open("bruja.png")
#Resize image
resimg=img.resize((400,250),Image.ANTIALIAS)
new_pic=ImageTk.PhotoImage(resimg)

my_label=Label(root,image=new_pic)
my_label.pack(pady=50)
root.mainloop()