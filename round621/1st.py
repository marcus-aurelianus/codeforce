import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,d = [int(x) for x in input().split()]
        *a, = [int(x) for x in input().split()]
        res=a[0]
        tempd=d
        for i in range(n-1):
            reqd=a[i+1]*(i+1)
            if tempd>reqd:
                tempd-=reqd
                res+=a[i+1]
            else:
                rreqd=tempd//(i+1)
                res+=rreqd
                break
        yield res

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
