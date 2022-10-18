from tkinter import *

from matplotlib.pyplot import fill
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")

my_menu=Menu(root)
root.config(menu=my_menu)

def our_command():
    my_label=Label(root,text="You clicked a dropdown menu!").pack()
    
def file_new():
    hide_frame()
    file_new_frame.pack(fill="both",expand=1)
    
def edit_cut():
    hide_frame()
    edit_cut_frame.pack(fill="both",expand=1)
    
def hide_frame():
    file_new_frame.pack_forget()
    edit_cut_frame.pack_forget()
#Create a menu item    
file_mennu=Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_mennu)
file_mennu.add_command(label="New...",command=file_new)
file_mennu.add_separator()
file_mennu.add_command(label="Exit",command=root.quit)


#Create an edit menu item
edit_menu=Menu(my_menu)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=edit_cut)
edit_menu.add_command(label="Copy",command=our_command)

#Create an options menu item
option_menu=Menu(my_menu)
my_menu.add_cascade(label="Options",menu=option_menu)
option_menu.add_command(label="Find",command=our_command)
option_menu.add_command(label="Find next",command=our_command)

#Create some frames
file_new_frame=Frame(root,width=400,height=400,bg="red")
edit_cut_frame=Frame(root,width=400,height=400,bg="blue")

#edit_cut_frame.winfo_children()  devueleve una lista de todos los hijos de este frame

root.mainloop()