import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,n,m = list(map(int,input().split()))
        if n+m>a+b:
            yield "No"
        else:
            if m<=min(a,b):
                yield "Yes"
            else:
                yield "No"
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


# 10 15 0 25
