import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def countit(lst,lenr):
    n=len(lst)
    counter=0
    if lenr>n:
        return 0
    else:
        subcounter=0
        for i in range(n):
            if lst[i]==1:
                subcounter+=1 
            else:
                if subcounter>=lenr:
                    counter+=(subcounter-lenr+1)
                subcounter=0
            if i==n-1:
                if subcounter>=lenr:
                    counter+=(subcounter-lenr+1)
    return counter
#print(countit([1,1,1,1],3))
        
if __name__ == '__main__':
    n,m,k = list(map(int,input().split()))
    a1=list(map(int,input().split()))
    a2=list(map(int,input().split()))
##    res=[]
##    for i in range(n):
##        res.append(list(map(lambda x:x*a1[i],a2)))
##    print(res)
    factk=list(factors(k))
    factk.sort()
    recdimen=[]
    for ele in factk:
        if ele<=(k**0.5):
            recdimen.append([ele,k//ele])
        else:
            break
    res=0
    #print(recdimen)
    for dima,dimb in recdimen:
        ta1,ta2=countit(a1,dima),countit(a2,dimb)
        tb1,tb2=countit(a2,dima),countit(a1,dimb)

        if dima==dimb:
            res+=(ta1*ta2)
        else:
            res+=(ta1*ta2+tb1*tb2)
    print(res)
