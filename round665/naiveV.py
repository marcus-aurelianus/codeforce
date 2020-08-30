import sys
input = sys.stdin.readline
mod=10**9+7
 
t=int(input())
for tests in range(t):
    n=int(input())
    E=[[] for i in range(n+1)]
 
    for i in range(n-1):
        x,y=map(int,input().split())
        E[x].append(y)
        E[y].append(x)
 
    m=int(input())
    V=sorted(map(int,input().split()))
 
    if m<=n-1:
        V=[1]*(n-1-m)+V
    else:
        X=1
        for j in range(m-n+1):
            X=X*V[-j-1]%mod
        V[n-2]=V[n-2]*X%mod
 
    TOP_SORT=[]
    Q=[1]
    USE=[0]*(n+1)
    USE[1]=1
    P=[-1]*(n+1)
    
    while Q:
        x=Q.pop()
        TOP_SORT.append(x)
        
        for to in E[x]:
            if USE[to]==0:
                Q.append(to)
                P[to]=x
                USE[to]=1
 
    L=[1]*(n+1)
 
    LIST=[]
    for x in TOP_SORT[1:][::-1]:
        LIST.append(L[x]*(n-L[x]))
        L[P[x]]+=L[x]
 
    LIST.sort()
 
    #print(V)
    #print(LIST)
 
    ANS=0
    for i in range(n-1):
        ANS=(ANS+LIST[i]*V[i])%mod
    print(ANS)
