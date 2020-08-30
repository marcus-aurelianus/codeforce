import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from copy import deepcopy

def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))
        arryS=deepcopy(arry)
        arryS.sort()
        minele=arryS[0]
        ans='YES'
        for i in range(n):
            if arry[i]==arryS[i] or arry[i]%minele==0:
                continue
            else:
                ans='NO'
                break
        
        yield ans
                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
