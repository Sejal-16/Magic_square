# -*- coding: utf-8 -*-



"""@author: chikoofudge
code about:dobble game
problem statement:create two lists such that in both the lists there is only one common element.ask the player 
to find out the the common symbol and display whether it is right or wrong."""
import string 
import random
symbols=[]
symbols=list(string.ascii_letters)
list1=[0]*5
list2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
print(pos1)
print(pos2)
samesymbol=random.choice(symbols)
symbols.remove(samesymbol)
if(pos1==pos2):
    list1[pos1]=samesymbol
    list2[pos1]=samesymbol
else:
    list1[pos1]=samesymbol
    list2[pos2]=samesymbol
    list1[pos2]=random.choice(symbols)
    list2[pos1]=random.choice(symbols)
    symbols.remove(list1[pos2])
    symbols.remove(list2[pos1])
i=0
while(i<5):
    if(i!=pos1 and i!=pos2):
        list1[i]=random.choice(symbols)
        symbols.remove(list1[i])
        list2[i]=random.choice(symbols)
        symbols.remove(list2[i])
        i=i+1
print(list1)
print(list2)
ans=input("enter the common symbol")
if(ans==samesymbol):
    print("right")
else:
    print("wrong")
print("thankyou")


