import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
from collections import defaultdict
def gift():
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        
        l = [0] * (n+1)
        ans = 0
     
        for j in range(n):
            r = [0] * (n+1)
            for k in range(n-1,j,-1):
                ans += l[a[k]] * r[a[j]]
                r[a[k]] += 1
  
            l[a[j]] += 1

     
        yield (ans)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)





#3 2 3 3


#1100
    
#1000
#    
