import sys
input = sys.stdin.readline
from collections import *
from heapq import *
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    a = [-1]*n
    pq = [(n, 0, n-1)]
    now = 1
    
    while now<=n:
        #print(pq)
        _, l, r = heappop(pq)
    
        if (r-l)%2==0:
            m = (l+r)//2
        else:
            m = (l+r-1)//2
        
        a[m] = now
        now += 1
        heappush(pq, (-(m-l), l, m-1))
        heappush(pq, (-(r-m), m+1, r))
 
    print(*a)
