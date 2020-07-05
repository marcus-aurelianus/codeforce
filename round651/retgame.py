import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def gift():
    for _ in range(t):
        n=int(input())
        if n==1:
            yield "FastestFinger"
        elif n==2:
            yield "Ashishgup"
        elif n%2:
            yield "Ashishgup"
        else:
            facti=sorted(list(factors(n)))
            found=False
            for ele in facti:
                if ele%2 and ele!=1:
                    found=True
                    break
            if found and len(facti)>4:
                yield "Ashishgup"
            else:
                yield "FastestFinger"

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


