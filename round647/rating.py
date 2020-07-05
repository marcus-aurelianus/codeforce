import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
def gift():
    for _ in range(t):
        n = int(input())
        bina=bin(n)[2:]
        lenn=len(bina)
        ans=0
        for i in range(lenn):
            if bina[i]=='1':
                ans+=(2**(lenn-i))-1
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
