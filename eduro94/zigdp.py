import sys
input = sys.stdin.readline
 
t=int(input())
for tests in range(t):
    n=int(input())
    A=list(map(int,input().split()))
 
    DP1=[0]*(n+1)
    DP2=[[0]*(n+1) for i in range(n+1)]
    DP3=[[0]*(n+1) for i in range(n+1)]
    DP4=[[0]*(n+1) for i in range(n+1)]
 
    for a in A:
        for i in range(1,n+1):
            DP4[i][a]+=DP3[i][a]
 
        for i in range(1,n+1):
            DP3[a][i]+=DP2[a][i]
 
        for i in range(1,n+1):
            DP2[i][a]+=DP1[i]
 
        DP1[a]+=1
 
    ANS=0
    for i in range(n+1):
        ANS+=sum(DP4[i])
    print(ANS)
