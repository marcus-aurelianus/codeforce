import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):

        n,m = list(map(int,input().split()))
        scores = list(map(int,input().split()))
        sumscore=sum(scores)
        if sumscore>=m:
            yield m
        else:
            yield sumscore
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
