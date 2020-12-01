import sys
from sys import stdin
 
tt = 1
 
for loop in range(tt):
 
    n = int(stdin.readline())
    a = list(map(int,stdin.readline().split()))
 
    if n > 100:
        print (1)
        continue
 
    ans = float("inf")
    for i in range(n):
 
        R = 0
        for r in range(i,n):
            R ^= a[r]
 
            L = 0
            for l in range(i-1,-1,-1):
                L ^= a[l]
                if L > R:
                    ans = min(ans,r-l-1)
 
    if ans == float("inf"):
        print (-1)
    else:
        print (ans)
