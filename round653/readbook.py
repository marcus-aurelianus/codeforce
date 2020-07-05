import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
from functools import reduce


n,k=list(map(int,input().split()))

temparry=[]

for i in range(3):
    temparry.append([0]*40000)

for i in range(n):
    t,a,b=list(map(int,input().split()))
    if a and b:
        temparry[0][t]+=1
    elif a:
        temparry[1][t*2]+=1
    elif b:
        temparry[2][t*2]+=1

ans=0
rema,remb=k,k
for i in range(20):
    print(i,rema,remb,ans)
    if rema and remb:
        if temparry[0][i]:
            freq=temparry[0][i]
            ans+=i

            tom=min(max(rema,remb),freq)

            temparry[0][i]=freq-tom
            rema=max(0,rema-tom)
            remb=max(0,remb-tom)
        if temparry[1][i]:         
            freq=temparry[1][i]
            tom=min(rema,freq)
            
            temparry[1][i]=freq-tom
            ans+=i//2
            rema=rema-tom
        if temparry[2][i]:
            freq=temparry[2][i]
            tom=min(remb,freq)
            
            temparry[2][i]=freq-tom
            ans+=i//2
            remb=remb-tom           
    if rema:
        if temparry[0][i]:
            freq=temparry[0][i]
            ans+=i
            rema=max(0,rema-freq)
        if temparry[1][i]:
            freq=temparry[1][i]

            tom=min(rema,freq)
            ans+=i//2
            temparry[1][i]-=tom
            rema-=tom
    if remb:
        if temparry[0][i]:
            freq=temparry[0][i]
            ans+=i
            remb=max(0,remb-freq)
        if temparry[2][i]:
            freq=temparry[2][i]
            tom=min(remb,freq)
            ans+=i//2
            temparry[2][i]-=tom
            remb-=tom
    if rema==0 and remb==0:
        break


if rema or remb:
    print(-1)
else:
    print(ans)







            
