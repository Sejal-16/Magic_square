# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:41:26 2020

@author: Hello User
programme name :montehall
"""
import random
doors=[0]*3
goatdoor=[0]*2
swap_win=0
noswap_win=0
x=random.randint(0,2)
doors[x]="BMW"
j=0
while(j<10):
    for i in range(0,3):
        if(x==i):
            continue
        else:
            doors[i]="goat"
            goatdoor.append(i)
    choice=int(input("player,enter your choice"))
    door_open=random.choice(goatdoor)
    while(door_open==choice):#whatever choice is of the user , we dont open that choice and open the reamining choice.
            door_open=random.choice(goatdoor)
    ch=input("do you want to swap y/n?")
    if(ch=="y"):
        if(doors[choice]=="goat"):
            print("you win")
            swap_win+=1
        else:
            print("you lost")
    else:
        if(doors[choice]=="goat"):
            print("you lost")
        else:
            print("you win")
            noswap_win+=1
print("no. of swap wins are:",swap_win)
print("no. of noswap wins are:",noswap_win)
        
        


