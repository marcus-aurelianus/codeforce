import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 

n=int(input())
fperm = list(map(int,input().split()))
sperm = list(map(int,input().split()))


tsperm=sperm+sperm

best=0
for i in range(n):
    curbest=0
    for j in range(n):
        if tsperm[i+j]==fperm[j]:
            curbest+=1
    best=max(best,curbest)
print(best)
