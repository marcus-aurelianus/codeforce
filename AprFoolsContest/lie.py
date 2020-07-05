import math
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

n=int(input())
inamo=list(factors(n))
inamo.sort()
ans=""
for ina in inamo:
    if ina!=1 and ina!=n:
        ans+=str(ina)
        ans+=str(n//ina)
        break
print(int(ans))



