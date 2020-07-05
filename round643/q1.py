import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,n = list(map(int,input().split()))
        for i in range(n-1):
            diu=list(str(a))
            dingding=int(min(diu))*int(max(diu))
            if dingding==0:
                break
            a+=dingding
        yield a
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
