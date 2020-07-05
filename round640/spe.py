import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arrys=list(map(int,input().split()))
        ans=[0]*(n+1)
        for i in range(n):
            now=arrys[i]
            for j in range(i+1,n):
                now+=arrys[j]
                if now<=n:
                    ans[now]=True
        res=0
        for i in range(n):
            if ans[arrys[i]]:
                res+=1
        yield res
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')



##100 55
##1 3 5
##33  22

##x+3*(k-x)=n
##n=3*k-2*x
##x=(3*k-n)//2
##1 3 1 3 1 3 49
            
