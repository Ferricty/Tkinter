from tkinter import *

root=Tk()

root.title("Ejemplo")

foto=PhotoImage(file="bruja.png")
Label(root,image=foto).pack()

frame=Frame(root)
frame.pack()

Label(frame, text="Elija destinos", width=50).pack()

Checkbutton(frame, text="Playa").pack()
Checkbutton(frame, text="Montaña").pack()
Checkbutton(frame, text="Desierto").pack()

root.mainloop()