import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
from functools import reduce


def gift():
    for _ in range(t):
        n=int(input())
        string=input()

        ans=0

        left=0
        for i in range(n):
            if string[i]=="(":
                left+=1
            else:
                left-=1
                if left<0:
                    ans+=1
                    left=0
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
