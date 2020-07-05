import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n,q = list(map(int,input().split()))
array = list(map(int,input().split()))
query = list(map(int,input().split()))

breakit=False
toremov=[]
for i in range(q):
    ele=query[i]
    if ele>0 or i==q-1:
        breakit=True
        
        m=len(toremove)
        removelst=[0]*m
        for j in range(m):
            for k in range(n):
                
            
            
