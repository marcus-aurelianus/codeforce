import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k= list(map(int,input().split()))
        mounts=list(map(int,input().split()))
        peak=[0]*n
        for i in range(1,n-1):
            if mounts[i]>mounts[i-1] and mounts[i]>mounts[i+1]:
                peak[i]=1
        fk=sum(peak[1:k-1])
        ans=1
        #print(peak,fk,peak[1:k-1])
        fktemp=fk
        for i in range(1,n-k+1):
            fiip=peak[i-1]
            fii=peak[i]
            fikp=peak[k+i-2]
            fik=peak[k+i-1]
            fktemp+=(fikp-fii)
            #print(fiip,fii,fikp,fik)
            if fktemp>fk:
                ans=i+1
                fk=fktemp
        yield str(fk+1)+" "+str(ans)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
