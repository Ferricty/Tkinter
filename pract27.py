#Text to speech
from tkinter import *
import pyttsx3
root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("400x500")

def talk():
    engine=pyttsx3.init()
    engine.say(myentry.get())
    engine.runAndWait()
    myentry.delete(0,END)
myentry=Entry(root,font=("Helvetica",18))
myentry.pack(pady=20)
mybtn=Button(root,text="Speak",command=talk)
mybtn.pack(pady=20)
root.mainloop()