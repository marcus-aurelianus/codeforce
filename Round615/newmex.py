import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from operator import itemgetter



n,m=map(int,input().split())

res=[0]*m
ans=0
for i in range(n):
    ele=int(input())
    res[ele%m]+=1

    #val,idx = min(enumerate(res), key=itemgetter(1))

    while (res[ans%m]):
        res[ans%m]-=1
        ans+=1
    print(res)

    print(ans)
