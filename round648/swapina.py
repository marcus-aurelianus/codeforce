import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 
def gift():
    for _ in range(t):
        n=int(input())
        eles = list(map(int,input().split()))
        types = list(map(int,input().split()))
        
        if sum(types)==0 or sum(types)==n:
            eleina=sorted(eles)
            if eleina==eles:
                yield 'YES'
            else:
                yield 'NO'
        else:
            yield 'YES'
            
        
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
