import sys
import io, os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
 
r,n=map(int,input().split())
C=[tuple(map(int,input().split())) for i in range(n)]
 
DP=[-1]*n
MAX=[-1]*n
 
for i in range(n):
    t,x,y=C[i]
    if t>=abs(x-1)+abs(y-1):
        DP[i]=1
    if t>r*2:
        MAX[i]=1
        break
 
for i in range(n):
    MAX[i]=max(MAX[i],MAX[i-1])
    
    play=max(MAX[i],DP[i])
 
    if play==-1:
        continue
    t0,x0,y0=C[i]
 
    for j in range(i+1,n):
        t,x,y=C[j]
        if t>=t0+abs(x-x0)+abs(y-y0):
            DP[j]=max(DP[j],play+1)
        if t>t0+r*2:
            MAX[j]=play+1
            break
 
ANS=max(max(MAX),max(DP))
 
if ANS==-1:
    print(0)
else:
    print(ANS)
