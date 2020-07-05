import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
from functools import reduce


def gift():
    for _ in range(t):
        n=int(input())
        counter=0
        while True:
            if n==1:
                break
            elif n%6==0:
                counter+=1
                n//=6
            elif n%3==0:
                counter+=2
                n//=3
            else:
                counter=-1
                break
        yield counter
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
