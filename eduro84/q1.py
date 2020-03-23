import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        kap=n**0.5
        if kap<k:
            yield 'NO'
        else:
            if (k+n)%2==0:
                yield "YES"
            else:
                yield 'NO'

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
