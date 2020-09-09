from sys import stdin
import sys
import math
 
n = int(stdin.readline())
 
a = [None] * (n+1)
 
l = 0
r = 1
 
for i in range(n-1):
 
    print ("?",l+1,r+1,flush=True)
    c1 = int(stdin.readline())
 
    print ("?",r+1,l+1,flush=True)
    c2 = int(stdin.readline())
 
    if c1 < c2: #c2 is m
        a[r] = c2
        r += 1
    else:
        a[l] = c1
        l = r
        r += 1
 
for i in range(n):
    if a[i] == None:
        a[i] = n
 
del a[n]
print ("!",*a,flush=True)
