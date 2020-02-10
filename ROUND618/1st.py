import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def sumproductzero():
    for _ in range(t):
        n = int(input())
        *a, = [int(x) for x in input().split()]
        n=a.count(0)
        sumall=sum(a)+n
        if sumall==0:
            yield n+1
        else:
            yield n
if __name__ == '__main__':
    t= int(input())
    ans = sumproductzero()
    print(*ans,sep='\n')
            
