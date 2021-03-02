import sys
from sys import stdin
 
tt = 1
 
for loop in range(tt):
 
    a,b,k = map(int,stdin.readline().split())
 
    if k == 0:
        print ("Yes")
        print ("1"*b + "0"*a)
        print ("1"*b + "0"*a)
 
    elif a == 0:
        if k > 0:
            print ("No")
        else:
            print ("Yes")
            print ("1"*b)
            print ("1"*b)
 
    elif a+b-1 <= k:
        print ("No")
 
    else:
        
 
        x = [None] * (a+b)
        y = [None] * (a+b)
 
        x[k] = "1"
        y[k] = "0"
        x[0] = "0"
        y[0] = "1"
 
        a -= 1
        b -= 1
 
        for i in range(len(x)):
            if x[i] != None:
                continue
            if a > 0:
                x[i] = "0"
                y[i] = "0"
                a -= 1
            else:
                x[i] = "1"
                y[i] = "1"
 
        x.reverse()
        y.reverse()
 
        
        x = "".join(x)
        y = "".join(y)
 
        if x[0] == y[0] == "1":
            print ("Yes")
            print (x)
            print (y)
        else:
            print ("No")
