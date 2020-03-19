import math
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
n,m=list(map(int,input().split()))
mod=998244353

def power(base,e):
    res=1
    while e:
        if e%2==1:
            res=res*base%mod;
        base=base*base%mod
        e//=2
    return res
if n==2:
    print(0)
else:
    ans,r=1,1
    for i in range(1,m+1):
        ans=ans*i%mod
    for i in range(1,n):
        r=r*i%mod
    for i in range(1,m-n+2):
        r=r*i%mod
    ans=math.factorial(m)%mod
 
    ans=ans*power(r,mod-2)%mod
    ans=ans*power(2,n-3)%mod*(n-2)%mod

    print(ans)
