import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from copy import deepcopy
def gift():
    for _ in range(t):
        n=int(input())
        arry=input()
        startp=None
        for i in range(n-1):
            if arry[i]=='1' and arry[i+1]=='0':
                startp=i
                break
        if startp==None:
            yield arry
        else:
            spoint=startp-1
            while spoint>=0:
                if arry[spoint]!='1':
                    break
                spoint-=1

            endpoint=n-1
            while endpoint>startp:
                if arry[endpoint]=='1':
                    endpoint-=1
                else:
                    break
            ans=arry[:(spoint+1)]+arry[endpoint:]
            yield ans
                    

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
