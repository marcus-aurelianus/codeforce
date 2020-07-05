import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from math import factorial
def gift():
    for _ in range(t):

        x1,y1,x2,y2 = list(map(int,input().split()))
        yield (y2-y1)*(x2-x1)+1
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
