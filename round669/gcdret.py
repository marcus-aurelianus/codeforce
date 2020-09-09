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
        n = int(input())
        arry = list(map(int,input().split()))
        arry.sort(reverse = True)
        start = arry[0]
        ans = [start]
        lst = sorted(list(factors(start)),reverse=True)
        index = 1
        arry.remove(start)
        gcd = lst
        while index<=n-1:
            found = False
            for ele in gcd:
                for aryelement in arry:
                    if aryelement % ele==0:
                        found = True
                        toremove = aryelement
                        break
                if found:
                    break
            ans.append(toremove)
            arry.remove(toremove)
            newlst = sorted(list(factors(toremove)),reverse=True)
            newgcd = []
            for divisor in newlst:
                if divisor in gcd:
                    newgcd.append(divisor)
            gcd = newgcd
            index += 1
                
        yield " ".join(str(x) for x in ans)

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
#1 0 1 0 1 0
