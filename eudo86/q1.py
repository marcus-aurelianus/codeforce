import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        x,y = list(map(int,input().split()))
        a,b = list(map(int,input().split()))
        if b>=2*a:
            yield (x+y)*a
        else:
            yield min(x,y)*b+(max(x,y)-min(x,y))*a

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
