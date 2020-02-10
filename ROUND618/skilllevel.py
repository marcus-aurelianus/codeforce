import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def skilllevel():
    for _ in range(t):
        n = int(input())
        *a, = [int(x) for x in input().split()]
        a.sort()
        yield a[n]-a[n-1]
if __name__ == '__main__':
    t= int(input())
    ans = skilllevel()
    print(*ans,sep='\n')
            
