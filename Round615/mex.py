import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from operator import itemgetter



n,m=map(int,input().split())

res=[0]*m

for i in range(n):
    ele=int(input())
    res[ele%m]+=1

    val,idx = min(enumerate(res), key=itemgetter(1))

    print(val+idx*m)
