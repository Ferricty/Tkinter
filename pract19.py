#tabs
from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")
def hide():
    my_notebook.hide(1)         #El 1 indica el indice del tab. como la roja fue la segunda tiene indice 1
    
def show():
    my_notebook.add(my_frame2,text="Red")
def select():
    my_notebook.select(1) 
my_notebook=ttk.Notebook(root)
my_notebook.pack(pady=10)
my_frame1=Frame(my_notebook,width=500,height=500,bg="blue")
my_frame2=Frame(my_notebook,width=500,height=500,bg="red")
my_frame1.pack(fill="both",expand=1)
my_frame2.pack(fill="both",expand=1)
my_notebook.add(my_frame1,text="Blue")
my_notebook.add(my_frame2,text="Red")
#Hide tab2
my_btn=Button(my_frame1,text="Hide tab Red",command=hide).pack(pady=10)
#Show tab2
my_btn2=Button(my_frame1,text="Show tab Red",command=show).pack(pady=10)
#Navigate to tab2
my_btn3=Button(my_frame1,text="Go to tab Red",command=select).pack(pady=10)
root.mainloop()