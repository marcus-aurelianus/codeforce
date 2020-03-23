import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

mod=998244353
if __name__ == '__main__':
    n,k= list(map(int,input().split()))
    array=list(map(int,input().split()))
    loc=[]

    for i in range(n):
        if array[i]>n-k:
            loc.append(i)
    m=len(loc)
    res=1
    for i in range(1,m):
        diff=loc[i]-loc[i-1]
        res=res*diff%mod
    print(str((n+n-k+1)*k//2)+" "+str(res))

            
