import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))
        arry.sort()
        if n%2==0:
            ansfound=False
            for i in range(1,n):
                diu=arry[0]^arry[i]
                cr=True
                for i in range(n):
                    fuk=arry[i]^diu
                    if fuk in arry:
                        continue
                    else:
                        cr=False
                        break
                if not cr:
                    continue
                else:
                    ansfound=True
                    
                if ansfound:
                    break
            if ansfound:
                yield diu
            else:
                yield -1
        else:
            yield -1
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
