import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b = list(map(int,input().split()))
        c=min(a,b)
        d=max(a,b)
        if c==d:
            yield (d*2)**2
        elif d>=2*c:
            yield d**2
        else:
            yield (c*2)**2

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
