import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,n = list(map(int,input().split()))
        c=n%a

        if c>=b:
            yield n-(c-b)
        else:
            yield n-c-(a-b)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
