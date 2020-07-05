import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

import math
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
inamo={2:1,3:2,5:3,7:4,11:5,13:6,17:7,19:8,23:9,29:10,31:11}
def gift():
    for _ in range(t):
        n=int(input())
        elements = list(map(int,input().split()))
        res=[]
        for ele in elements:
            for num in inamo:
                if ele%num==0:
                    res.append(inamo[num])
                else:
                    res.append()

        
    
##if __name__ == '__main__':
##    t= int(input())
##    ans = gift()
##    print(*ans,sep='\n')

ele=range(2,12)
res={}
for i in range(4,1001):
    kap=list(factors(i))
    kap.sort()
    res[kap[1]]=True
print(res)
