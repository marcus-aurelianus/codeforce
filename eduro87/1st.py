import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,c,d = list(map(int,input().split()))
        if b>=a:
            yield b
        else:
            if d>=c:
                yield -1
            else:
                didi=(a-b)%(c-d)
                bibi=(a-b)//(c-d)
                if didi:
                    bibi+=1
            
                yield bibi*c+b
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
