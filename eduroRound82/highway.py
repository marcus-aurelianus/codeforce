import sys

reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def highway():
    for _ in range(t):
        n,g,b=map(int,input().split())
        if n%2==0:
            half=n//2
        else:
            half=n//2+1
        otherhalf=n-half
        if half//g==0:
            yield n
        else:
            if half%g==0:
                otherhalfcommit=(half//g-1)*(b)
                if otherhalfcommit<otherhalf:
                    yield (half//g-1)*(g+b)+(half-(half//g-1)*g)+(otherhalf-otherhalfcommit)
                else:
                    yield (half//g-1)*(g+b)+(half-(half//g-1)*g)
            else:
                otherhalfcommit=(half//g)*b
                if otherhalfcommit<otherhalf:
                    yield (half//g)*(g+b)+(half%g)+(otherhalf-otherhalfcommit)
                else:
                    yield (half//g)*(g+b)+(half%g)
        
if __name__ == '__main__':
    t= int(input())
    ans = highway()
    print(*ans,sep='\n')
            
