# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 18:51:18 2020
@author:chikoofudge
problem statement:print a n row by n column matrix representing numbers from 1 to 9 ..such that the sum of all the rows and columns and diagnols will be n(n^2+1)/2
algorithm:1)sum=n(n^2+1)/2 for every column and row and diagnol when numbers are placed.
2)lets say position of 1 is (n/2,n-1) is (p,q) the next number which is 2 is located at ((p-1),(p-2)) position.
anytime if the calculated position row position becomes -1 then make it (n-1) and if column position becomes n then make it zero.
3)if the calculated position already contains a number then decrement the column by 2 and increment the row by 1.
4)if anytime the row position becomes -1 and column position becomes n switch it to (0,n-2).
"""
def magic(n):
  magicSquare=[]

  for i in range(n):
    sub_list=[]
    for j in range(n):
        sub_list.append(0)
    magicSquare.append(sub_list)
  i=n//2
  j=n-1
  count=1
  num=n*n
  while(count<=num):
     if(i==-1 and j==n):  #condition 4 inside the algorithm 
        i=0
        j=n-2
     elif(i<0): #condition2 2nd part inside the algo
        i=n-1
     elif(j==n): #condition2 3rd part inside the algo
        j=0
     if(magicSquare[i][j]!=0): #condition3 inside the algo
         j=j-2
         i=i+1
         continue
     else:
         magicSquare[i][j]=count
         count=count+1
     i=i-1
     j=j+1 #condition 2 1st part inside the algo 
  for i in range(n):
      for j in range(n):
          print(magicSquare[i][j],end=" ")
      print()
magic(3)
    
     
    
        
    

