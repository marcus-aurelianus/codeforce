import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
from functools import reduce


n,k=list(map(int,input().split()))

temparry=[]

for i in range(3):
    temparry.append([0]*10001)

for i in range(n):
    t,a,b=list(map(int,input().split()))
    if a and b:
        temparry[0][t]+=1
    elif a:
        temparry[1][t]+=1
    elif b:
        temparry[2][t]+=1

ans=0
rema,remb=k,k
for i in range(10001):
    if rema and remb:
        freq=temparry[0][i]
        if freq:
            
            timus=min(rema,freq)
            rema-=timus
            remb-=timus
            ans+=(i*timus)
            temparry[0][i]-=timus
    if rema==0:
        break

#print(temparry[0][:20])
#print(temparry[1][:20])
#print(temparry[2][:20])
if rema or remb:
    for i in range(10001):
        #print(i,ans,temparry[0][i],rema,remb)
        if rema:
            freq0=temparry[0][i]
            freq1=temparry[1][i]
            tominus=min(freq0+freq1,rema)
            if tominus:
                rema-=tominus
                ans+=(i*tominus)
        if remb:
            freq0=temparry[0][i]
            freq2=temparry[2][i]
            tominus=min(freq0+freq2,rema)
            if tominus:
                remb-=tominus
                ans+=(i*tominus)
        if rema==0 and remb==0:
            break
    if rema or remb:
        print(-1)
    else:
        print(ans)
else:
    print(ans)







            
