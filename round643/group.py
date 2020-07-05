import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        dudes = list(map(int,input().split()))
        res={}
        for kap in dudes:
            freq=res.get(kap,0)
            res[kap]=freq+1
        ans=0
        keys=list(res.keys())
        keys.sort()
        ans=0
        nex=0
        for k in keys:
            #print(nex,ans,res[k],k)
            ans+=(res[k]+nex)//k
            nex=(res[k]+nex)%k

        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
