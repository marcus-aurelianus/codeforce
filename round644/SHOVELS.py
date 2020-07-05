import math
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):

        n,k = list(map(int,input().split()))
        factorino=list(factors(n))
        factorino.sort(reverse=True)
        for kap in factorino:
            if kap<=k:
                yield n//kap
                break

        
            

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
