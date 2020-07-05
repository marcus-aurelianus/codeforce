import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

from copy import deepcopy

n,k=list(map(int,input().split()))
arry=list(map(int,input().split()))


if n==2 or k==2:
    print(min(arry))
else:
    index=k//2
    arrc=deepcopy(arry)
    arrc.sort()
    kth=arrc[index-1]
    kthm1=arrc[index-2]
    kthp1=arrc[index]
    near=False
    m1loc={}
    m2loc={}
    for i in range(n):
        if arry[i]==kthm1:
            m1loc[i]=True
        if arry[i]==kth:
            m2loc[i]=True
    for j in m2loc:
        b1=m1loc.get(j-1,False)
        p1=m1loc.get(j+1,False)
        if b1 or p1:
            near=True
            break
    if near:
        print(kthp1)
    else:
        print(kth)
        
    

# 1 9 2 8 7 5 2 2 6 10 11

# 5 3 2 5 50 5


