import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m,a,b = list(map(int,input().split()))
        if b<n-(m-a):
            yield 'NO'
        else:
            
            yield 'YES'
            for i in range(n):
                startpos=(b*i)%m
                yield '0'*startpos+'1'*a+(m-startpos-a)*'0'
    
#111000
#011100
#101100
#110100
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
