from random import randint
import random

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

answer=our_states[rando]
'''
# add our first random selection to our answer_list list
answer_list.append(our_states[rando])

#print(our_states)

#remove answer from list
our_states.remove(our_states[rando])

print(our_states)

random.shuffle(our_states)
#print(our_states)

#Randomly select our next state

rando=randint(0,len(our_states)-1)
answer_list.append(our_states[rando])

#Remove second answer from list
our_states.remove(our_states[rando])

random.shuffle(our_states)
'''
count=1
while count<4:
    rando=randint(0,len(our_states)-1)
    
    #if first selection make it our answer
    if count==1:
        answer=our_states[rando]
    answer_list.append(our_states[rando])
    our_states.remove(our_states[rando])
    random.shuffle(our_states)
    count+=1

print(answer_list)
print(answer)
random.shuffle(answer_list)
print(answer_list)


