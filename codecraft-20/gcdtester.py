a=[3,5,2]
b=[5,3,1]
n=len(a)
m=len(b)
res=[]
for i in range(n+m-1):
    currcoeff=0
    for j in range(min(i+1,n)):
        #print(i,j)
        if i-j<=m-1:
            currcoeff+=(a[j]*b[i-j])
    res.append(currcoeff)

print(a)
print(b)
print(res)


import math
def is_prime(n):
    if n % 2 == 0 and n > 2: 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


for ele in res:
    print(ele,is_prime(ele))
    #print(factors(ele))
