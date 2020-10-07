import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

n,m = list(map(int,input().split()))

robbers = []
searchers = []

for i in range(n):
    cord = list(map(int,input().split()))
    robbers.append(cord)
    
for i in range(m):
    cord = list(map(int,input().split()))
    searchers.append(cord)

xMax, yMax = 0, 0

tou = defaultdict(lambda:0)

maxIt = 0
for robber in robbers:
    rx, ry = robber
    for searcher in searchers:
        sx,sy = searcher

        dx, dy = sx-rx, sy-ry
        
        if dx>=0 and dy>=0:
            tou[dx+1]=max(tou[dx+1],dy+1)

if len(tou)==0:
    print(0)
else:
    dingDong = sorted(tou.items ())
    dingDongBack = sorted(tou.items (),key=lambda x:x[1])
    m = len(dingDong)
    #print(dingDong,dingDongBack)
    if m==1:
        print(min(dingDong[-1][0],dingDong[-1][1]))
    else:
        maxSofarBack = 0
        maxSofarFront = 0
        minAns = min(dingDong[-1][0],dingDongBack[-1][1])
        for i in range(1,m):
            maxSofarBack = max(maxSofarBack,dingDong[m-i][1])
            minAns = min(minAns,maxSofarBack+dingDong[m-1-i][0])

            maxSofarFront = max(maxSofarFront,dingDongBack[m-i][0])
            minAns = min(minAns,maxSofarFront+dingDongBack[m-1-i][1])      
        print(minAns)   
        



#"{} {} {}".format(maxele,minele,minele)
