from tkinter import *
from PIL import ImageTk,Image
import numpy as np
import matplotlib.pyplot as plt


root=Tk()
root.title("Practicando")
root.iconbitmap("bruja.ico")
root.geometry("400x200")

def graph():
    precios_de_casas=np.random.normal(200000, 25000, 5000)
    plt.hist(precios_de_casas,50)
    plt.show()
graph_btn=Button(root,text="Graficar", command=graph)
graph_btn.pack()
root.mainloop()
