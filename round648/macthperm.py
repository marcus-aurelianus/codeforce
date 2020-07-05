import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 

n=int(input())
fperm = list(map(int,input().split()))
sperm = list(map(int,input().split()))


tperm=sperm+sperm+[0]


s=0
best=0
curr=1
dic={}

for i in range(n):
    dic[fperm[i]]=i

while s<(2*n):
    ele=tperm[s]
    pos=dic[ele]
    if pos!=n-1:
        if tperm[s+1]==fperm[pos+1]:
            curr+=1
    else:
        best=max(best,curr)
        curr=1
    s+=1
print( best)
            
            
        
        

