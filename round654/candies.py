import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from math import factorial
def nPr(n, r):
    return int(factorial(n)/factorial(n-r))

n,p = list(map(int,input().split()))

#arry = list(map(int,input().split()))


print(nPr(n,p))




##4 3 3 3
##4 3 3 3
##
##14
### 10 15 0 25
##1 0 0 0 0
##0 1 0 0 0
##0 0 1 0 0
##0 0 0 1 0
##0 0 0 0 1
