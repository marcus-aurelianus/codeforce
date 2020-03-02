import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        x,y,a,b= [int(x) for x in input().split()]
        if (y-x)%(a+b)==0:
            yield( y-x)//(a+b)
        else:
            yield -1

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
