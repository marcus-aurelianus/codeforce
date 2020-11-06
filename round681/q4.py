import sys
from sys import stdin
 
tt = int(stdin.readline())
 
for loop in range(tt):
 
    n = int(stdin.readline())
    a = list(map(int,stdin.readline().split()))
 
    r = a[0]
    l = 0
 
    for i in range(n):
 
        if r + l < a[i]:
            l = a[i] - r
        elif r + l > a[i]:
            r = a[i] - l
 
    if r >= 0:
        print ("YES")
    else:
        print ("NO")
