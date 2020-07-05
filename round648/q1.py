import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        zcount=0
        kappre=[0]*m
        kappri=[0]*n
        didi=[]
        for i in range(n):
            kap=list(map(int,input().split()))
            didi.append(kap)
            for j in range(m):
                if kap[j]==1:
                    kappre[j]=1
                    kappri[i]=1
        for i in range(n):
            for j in range(m):
                if didi[i][j]==0 and kappre[j]==0 and kappri[i]==0:
                    #print(i,j)
                    zcount+=1
                    kappre[j]=1
                    kappri[i]=1
        #yield zcount
        if zcount%2:
            yield "Ashish"
        else:
            yield "Vivek"
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
