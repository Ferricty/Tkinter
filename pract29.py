#Progress bar
from tkinter import *
from tkinter import ttk
import time
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")

def step():
    #my_progress['value']+=20
    #my_progress.start(10)
    for x in range(5):
        my_progress['value']+=20
        root.update_idletasks()
        time.sleep(1)
    
def stop():
    my_progress.stop()
my_progress=ttk.Progressbar(root,orient=HORIZONTAL,length=300,mode='determinate')
my_progress.pack(pady=20)
btn=Button(root,text="Progress",command=step)
btn.pack(pady=20)
btn2=Button(root,text="Stop",command=stop)
btn2.pack(pady=20)

root.mainloop()