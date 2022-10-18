#Movimiento con Canvas
from tkinter import *

root=Tk()
root.title("Practicando tkinter")
root.iconbitmap("bruja.ico")
root.geometry("500x500")

w=600
h=400

x=w//2
y=h//2
my_canvas=Canvas(root,width=w,height=h,bg="white")
my_canvas.pack(pady=20)
img=PhotoImage(file="login.png")
my_img=my_canvas.create_image(260,125,anchor=NW,image=img)
# def left(event):
#     x=-10
#     y=0
#     my_canvas.move(my_img,x,y)
# def right(event):
#     x=10
#     y=0
#     my_canvas.move(my_img,x,y)
# def up(event):
#     x=0
#     y=-10
#     my_canvas.move(my_img,x,y)
# def down(event):
#     x=0
#     y=10
#     my_canvas.move(my_img,x,y)
# root.bind("<Left>",left)
# root.bind("<Right>",right)
# root.bind("<Up>",up)
# root.bind("<Down>",down)
def move(e):
    global img
    img=PhotoImage(file="login.png")
    my_img=my_canvas.create_image(e.x,e.y,image=img)
    my_label.config(text="Coordinates x: {} y: {}".format(e.x,e.y))
my_label=Label(root,text="")
my_label.pack(pady=20)
my_canvas.bind("<B1-Motion>",move)

root.mainloop()