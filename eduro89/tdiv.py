import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__



import math
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


#print(factors(49))
n= int(input())
nums=list(map(int,input().split()))

diff=0.1**10

ans1=[]
ans2=[]
for i in range(n):
    kap=list(factors(nums[i]))

    if len(kap)==2:
        ans1.append(-1)
        ans2.append(-1)
    else:
        kap.sort()

        brino=kap[1]
        didi=math.log(nums[i],brino)

        didim=round(didi)
        if abs(didi-didim)<diff:
            ans1.append(-1)
            ans2.append(-1)
        else:
            ans1.append(kap[1])
            ans2.append(kap[2])
print(" ".join(str(x) for x in ans1))
    
print(" ".join(str(x) for x in ans2))

# 2x+y<a
# 2y+x<b

#3x+3y<a+b
#x<
            
