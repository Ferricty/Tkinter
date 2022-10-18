#Imagenes como botones
from tkinter import *

root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("500x500")
def thing():
    mylabel.config(text="You clicked the button")
login_btn=PhotoImage(file="login.png")
img_label=Label(image=login_btn)
#img_label.pack(pady=20)
btn=Button(root,image=login_btn,command=thing,borderwidth=0)
btn.pack(pady=20)
mylabel=Label(root,text="")
mylabel.pack(pady=20)
root.mainloop()