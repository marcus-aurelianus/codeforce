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
    ans=1*(n-2)*power(2,n-3)%mod
    for i in range(1,n):
        ans=ans*(m-i+1)%mod*power(i,mod-2)%mod

    print(ans)
print(power(2,20))
