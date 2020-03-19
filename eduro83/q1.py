import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b = list(map(int,input().split()))
        if a%b==0:
            yield 'YES'
        else:
            yield 'NO'


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
