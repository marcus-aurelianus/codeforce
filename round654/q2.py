import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,r = list(map(int,input().split()))
        if n>r:
            yield (r+1)*r//2
        else:
            yield (n)*(n-1)//2+1
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
