import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        x,y,z = list(map(int,input().split()))

        maxele=max(x,y,z)
        minele=min(x,y,z)
        midele=x+y+z-maxele-minele

        if midele==maxele:
            yield 'YES'

            yield "{} {} {}".format(maxele,minele,minele)
        else:
            yield 'NO'
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
