import sys
import math
from functools import reduce
import bisect

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def factors(n):    
    return sorted(list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))))



def gift():
    for _ in range(cou):
        a,b,c=map(int,input().split())

        resa,resb,resc=-1,-1,-1
        changed=float("inf")
        for inamo in range(1,max(a,b,c)+1):
            factorino=factors(inamo)

            loc=bisect.bisect_right(factorino,a)
            if loc==len(factorino):
                loc-=1
            tempa=factorino[loc]
            
            tempb=inamo
            recinamo=inamo-c%inamo
            if c<inamo:
                tempc=inamo
            else:
                if c%inamo>=recinamo:
                    tempc=c+recinamo
                else:
                    tempc=c-c%inamo
            
            nowdis=abs(a-tempa)+abs(b-tempb)+abs(c-tempc)
            if nowdis<changed:
                resa,resb,resc=tempa,tempb,tempc
                changed=nowdis
            print(nowdis,tempa,tempb,tempc,recinamo,c%inamo)
            
        yield str(resa)+" "+str(resb)+" "+str(resc)
            
            
        

if __name__ == '__main__':
    cou= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
