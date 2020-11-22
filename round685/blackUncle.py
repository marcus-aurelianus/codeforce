import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        d,k = list(map(int,input().split()))
        s = (d*(2**0.5)/2)//k*k
        if ((s+k)**2+s**2)**0.5>d:
            yield 'Utkarsh'
        else:
            yield 'Ashish'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
