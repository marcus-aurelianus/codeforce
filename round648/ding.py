import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 
 
n=int(input())
fperm = list(map(int,input().split()))
sperm = list(map(int,input().split()))
 
 
 
 
diu=[0]*n


for i in range(n):
    diu[fperm[i]-1]+=i
    diu[sperm[i]-1]-=i
 
 
out=[0]*n


for v in diu:
    out[v]+=1
print(max(out))
