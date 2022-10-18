from tkinter import *

from matplotlib.pyplot import fill
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")

#Creando paneles
panel1=PanedWindow(bd=4,relief="raised",bg="red")
panel1.pack(fill=BOTH,expand=1)
l_panel1=Label(panel1,text="Left Panel")
panel1.add(l_panel1)

#Creando segundo panel
panel2=PanedWindow(panel1,orient=VERTICAL,bd=4,relief="raised",bg="blue")
panel1.add(panel2)
top=Label(panel2,text="Top Panel")
panel2.add(top)
bottom=Label(panel2,text="Bottom Panel")
panel2.add(bottom)
root.mainloop()