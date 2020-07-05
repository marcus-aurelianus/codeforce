import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        for i in range(n-2):
            if i%2==0:
                yield 'BW'*(m//2)+'B'*(m%2)
            else:
                yield 'WB'*(m//2)+'W'*(m%2)
        if n%2==0:
            yield 'W'*(m%2)+'WB'*(m//2)
            yield 'B'*(m%2)+'BW'*(m//2-1)+'BB'
        else:
            yield 'W'*(m%2)+'BW'*(m//2)
            yield 'BB'+'W'*(m%2)+'BW'*(m//2-1)
                
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            

