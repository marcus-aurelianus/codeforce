import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())

        a=list(map(int,input().split()))

        res=True
        for i in range(n):
            if a[i*2]>n+i or a[i*2+1]>n+i+1:
                res=False
                break
        yield 'YES' if res else 'NO'
                

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
