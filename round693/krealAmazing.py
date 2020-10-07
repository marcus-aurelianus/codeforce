import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
     
        lis  = [0] * (n+1)
        md   = [float("-inf")] * (n+1)
     
        for i in range(n):
     
            md[a[i]] = max(md[a[i]] , (i+1)-lis[a[i]])
            lis[a[i]] = i+1
        print (md)
        for i in range(n+1):
            md[i] = max(md[i] , n+1-lis[i])
     
        print (md)
        
        itr = n-1
        ans = [-1] * n
     
        for i in range(1,n+1):
     
            while md[i] <= itr+1:
                ans[itr] = i
                itr -= 1
        yield " ".join(str(x) for x in ans)
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
