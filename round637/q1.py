import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,a,b,c,d = list(map(int,input().split()))
        minn=n*(a-b)
        maxn=n*(a+b)
        if (minn<=c+d and maxn>=c-d) :
            yield 'Yes'
        else:
            yield 'No'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
