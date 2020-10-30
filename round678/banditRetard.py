import sys
input = sys.stdin.readline
import math

n=int(input())
P=[1]+list(map(int,input().split()))
A=list(map(int,input().split()))
 
for i in range(n):
    P[i]-=1
 
Y=[1]*n
for i in range(n):
    Y[P[i]]=0
 
#print(Y)
 
for i in range(n-1,0,-1):
    Y[P[i]]+=Y[i]
 
S=[a for a in A]
for i in range(n-1,0,-1):
    S[P[i]]+=S[i]
 

ans = 0
for i in range(n):
    ans = max(ans,math.ceil(S[i]/Y[i]))
print(ans)

