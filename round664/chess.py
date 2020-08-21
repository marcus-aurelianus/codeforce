import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n,m,x,y = list(map(int,input().split()))

res=[]
res.append([x,y])

for i in range(m):
    if i!=y-1:
        res.append([x,i+1])
        
for i in range(n):
    last=res[-1]
    lasx,lasy=last
    if i!=x-1:
        res.append([i+1,lasy])
        for j in range(m):
            if j!=lasy-1:
                res.append([i+1,j+1])
for ans in res:
    print(" ".join(str(x) for x in ans))
        
