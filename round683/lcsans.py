import io,os
from math import *
 
n, m = map(int, input().split())
a = input()
b = input()
 
LR = [0 for _ in range(n+1)]
 
best = 0
for c in b:
    NR = [0 for _ in range(n+1)]
    for i in range(1,n+1):
        back = NR[i-1] - 1
        up = LR[i] - 1
        diag = LR[i-1] - 2
        if c == a[i-1]:
                diag += 4
        NR[i] = max(back, up, diag, 0)
        best = max(best, NR[i])
    #print(LR)
    LR = NR
#print(NR)
print(best)
