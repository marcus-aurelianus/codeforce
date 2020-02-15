import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a=input()
        b=input()
        c=input()
        n=len(a)
        canswap=True
        for i in range(n):
            if a[i]==c[i] or b[i]==c[i]:
                continue
            else:
                canswap=False
                break
        if canswap:
            yield 'YES'
        else:
            yield 'NO'
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
