import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
t=int(input())
for tests in range(t):
    n=int(input())
    A=list(map(int,input().split()))
 
    COUNT=[[0]*27 for i in range(n)]
 
    for i in range(n):
        for j in range(1,27):
            COUNT[i][j]=COUNT[i-1][j]
        COUNT[i][A[i]]+=1
 
    ANS=1
    print(COUNT)
 
    for i in range(1,27):
        bind=0
        eind=n-1
        score=0
 
        while bind<eind:
            while bind<n and A[bind]!=i:
                bind+=1
            while eind>=0 and A[eind]!=i:
                eind-=1
            #print(i,bind,eind)
            if bind<eind:
                score+=2
 
                C=[0]*27
                for j in range(27):
                    C[j]=COUNT[eind-1][j]-COUNT[bind][j]
                    
                ANS=max(ANS,score+max(C))
                #print(ANS,i,bind,eind,score)
 
                bind+=1
                eind-=1
    print(ANS)
