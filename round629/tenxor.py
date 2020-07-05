import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math

def gift():
    for _ in range(t):
        n=int(input())
        num=input()
        ans1=['1']
        ans2=['1']
        for i in range(1,n):
            if num[i]=='0':
                ans1.append('0')
                ans2.append('0')
            elif num[i]=='2':
                ans1.append('1')
                ans2.append('1')
            else:
                ans1.append('1')
                ans1+=[0]*(n-i-1)
                ans2.append('0')
                ans2+=list(num[i+1:n+1])
                break
        yield "".join(str(x) for x in ans1)
        yield "".join(str(x) for x in ans2)
     
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
