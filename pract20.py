#Creating multiple entry box
from tkinter import *

root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("700x500")

myentrys=[]
def something():
    entry_list=''
    for entries in myentrys:
        entry_list+=str(entries.get())+'\n'
        mylabel.config(text=entry_list)
#Creating rows
for y in range(5):
    #Creating columns        
    for x in range(5):
        myentry=Entry(root)       
        myentry.grid(row=y,column=x,pady=20,padx=5)
        myentrys.append(myentry)
mybtn=Button(root,text="Click Me!",command=something)
mybtn.grid(row=5,column=0,pady=20)
mylabel=Label(root,text='')
mylabel.grid(row=6,column=0,pady=20)
root.mainloop()