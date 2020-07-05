import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m,k = list(map(int,input().split()))


        divis=n//k


        maxjok=min(divis,m)
        didi=(m-(maxjok))%(k-1)
        minjok=(m-(maxjok))//(k-1)
        #print(maxjok,didi,minjok,n,m,k)
        if didi:
            minjok+=1
        yield maxjok-minjok
            
        

        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
