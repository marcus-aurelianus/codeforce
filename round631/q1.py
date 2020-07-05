import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,x = list(map(int,input().split()))
        arry=list(map(int,input().split()))
        ans=[0]*(n+x)
        
        for ele in arry:
            if ele<=(n+x):
                ans[ele-1]=1
        res=None
        #print(ans)
        xcop=x
        for i in range(n+x):
            if ans[i]==0:
                if xcop>0:
                    xcop-=1
                else:
                    res=i
                    break
        #print(res,n,x)
        if not res:
            res=n+x
    
        yield res

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
