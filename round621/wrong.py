import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
 
def hop():
    for _ in range(t):
        n,dis = [int(x) for x in input().split()]
        *a, = [int(x) for x in input().split()]
        maxhop=max(a)
        if dis in a:
            yield 1
        else:
            if dis%maxhop==0:
                yield dis//maxhop
            else:
                yield max(dis//maxhop+1,2)
        
 
if __name__ == '__main__':
    t= int(input())
    ans = hop()
    print(*ans,sep='\n')
            
