from tkinter import *
from PIL import ImageTk,Image
from random import randint
import random

from django.http import response
root=Tk()
root.title("Practicando")
root.iconbitmap("bruja.ico")
root.geometry("500x500")


def state_capital_answer():
    if capital_radio.get()==our_state_capitals[answer]:
        response="correct"
    else:
        response="incorrect"
    answer_label_capitals.config(text=response)
        



def random_state():
    
    
    #Create list of state names
    global our_states
    our_states=["california","florida","illinois","kentucky","nebraska"] 
    global rando
    #Generate random number
    rando=randint(0,len(our_states)-1)
    state="states/"+our_states[rando]+".png"
    

    #Create our State Images
 
    global state_image
  
    state_image=ImageTk.PhotoImage(Image.open(state))
    show_state.config(image=state_image)








#Create answer function
def state_answer():
    answer=answer_input.get()
    answer=answer.replace(" ","")
    if answer.lower()==our_states[rando]:
        response="Correct"
    else:
        response="Incorrect"
    answer_label.config(text=response)
    #Clear answer
    answer_input.delete(0,END)
    random_state()

#Create State Flashcard Function
def states():
    hide_all_frames()
    state_frame.pack(fill="both",expand=1)
    #my_label=Label(state_frame,text="States").pack()
    
    
    # #Create list of state names
    # global our_states
    # our_states=["california","florida","illinois","kentucky","nebraska"] 
    # global rando
    # #Generate random number
    # rando=randint(0,len(our_states)-1)
    # state="states/"+our_states[rando]+".png"
    

    # #Create our State Images
    # global img
    # img=Image.open(state)
    # global state_image
    # global show_state
    # res_img_b1=img.resize((10,10))
    # state_image=ImageTk.PhotoImage(res_img_b1)
    global show_state
    show_state=Label(state_frame)
    show_state.pack(pady=15)
    random_state()
    
    #Create answer input box
    global answer_input
    answer_input=Entry(state_frame, font=("Helvetica",18))
    answer_input.pack(pady=15)
    
    
    
    
    #Create Button to Randomize State Images
    rando_button=Button(state_frame,text="Pass",command=states)
    rando_button.pack(pady=10)
    
    #Create a Button to Answer the question
    answer_button=Button(state_frame,text="Answer",command=state_answer)
    answer_button.pack(pady=5)
    
    global answer_label
    #Create a Label to tell if answer is correct or not
    answer_label=Label(state_frame,text="",font=("Helvetica",18))
    answer_label.pack(pady=15)
    
    

#Create State Capital Flashcard Function
def state_capitals():
    hide_all_frames()
    state_capitals_frame.pack(fill="both",expand=1)
    #my_label=Label(state_capitals_frame,text="State Capitals").pack()
    global show_state
    show_state=Label(state_capitals_frame)
    show_state.pack(pady=15)
    answer_list=[]
    global our_states
    our_states=["california","florida","illinois","kentucky","nebraska"] 

    global our_state_capitals
    our_state_capitals={
        "california":"sacramento",
        "florida":"tallahassee",
        "illinois":"springfield",
        "kentucky":"frankfort",
        "nebraska":"lincoln"
    }

    #Generate random number
    rando=randint(0,len(our_states)-1)

    # print(our_state_capitals[our_states[rando]])
    global answer
    answer=our_states[rando]

    count=1
    while count<4:
        rando=randint(0,len(our_states)-1)
        
        #if first selection make it our answer
        if count==1:
            
            answer=our_states[rando]
            global state_image
            state="states/"+our_states[rando]+".png"
            state_image=ImageTk.PhotoImage(Image.open(state))
            show_state.config(image=state_image)
        answer_list.append(our_states[rando])
        our_states.remove(our_states[rando])
        random.shuffle(our_states)
        count+=1
    random.shuffle(answer_list)
    
    global capital_radio
    #capital_radio=IntVar()
    capital_radio=StringVar()
    capital_radio.set(our_state_capitals[answer_list[0]])
    capital_radio_button1=Radiobutton(state_capitals_frame,text=our_state_capitals[answer_list[0]].title(),variable=capital_radio,value=our_state_capitals[answer_list[0]]).pack()
    capital_radio_button2=Radiobutton(state_capitals_frame,text=our_state_capitals[answer_list[1]].title(),variable=capital_radio,value=our_state_capitals[answer_list[1]]).pack()
    capital_radio_button3=Radiobutton(state_capitals_frame,text=our_state_capitals[answer_list[2]].title(),variable=capital_radio,value=our_state_capitals[answer_list[2]]).pack()
    pass_button=Button(state_capitals_frame,text="pass",command=state_capitals)
    pass_button.pack(pady=15)
    
    capital_submit_button=Button(state_capitals_frame,text="Answer",command=state_capital_answer)
    capital_submit_button.pack()
    global answer_label_capitals
    answer_label_capitals=Label(state_capitals_frame,text="",font=("Helvetica",18))
    answer_label_capitals.pack(pady=15)
    
    
    
    
#Hide all previus frames
def hide_all_frames():
    #Loop thru and destroy all children in previus frames
    for widget in state_frame.winfo_children():
        widget.destroy()
        
    for widget in state_capitals_frame.winfo_children():
        widget.destroy()
    state_frame.pack_forget()
    state_capitals_frame.pack_forget()




#Create menu
my_menu=Menu()
root.config(menu=my_menu)

#Create menu items
states_menu=Menu(my_menu)
my_menu.add_cascade(label="Geography",menu=states_menu)
states_menu.add_command(label="States",command=states)
states_menu.add_command(label="State Capitals",command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit",command=root.quit)

state_frame=Frame(root,width=500,height=500)
state_capitals_frame=Frame(root,width=500,height=500)

mainloop()



