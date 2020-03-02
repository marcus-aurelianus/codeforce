import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,c = [int(x) for x in input().split()]
        lst=[a,b,c]
        count0=lst.count(0)
        count1=lst.count(1)
        count2=lst.count(2)
        count3=lst.count(3)
        minx=min(lst)
        maxx=max(lst)
        sumx=sum(lst)
        midx=sumx-maxx-minx
        if minx>=4:
            yield 7
        elif minx==3:
            yield 6
        elif minx==2:
            if maxx>=3:
                yield 5
            else:
                yield 4
        elif minx==1:
            if maxx>=2:
                if midx>=2:
                    yield 4
                else:
                    yield 3
            else:
                yield 3
        else:
            if maxx>=2:
                if midx>=2:
                    yield 3
                elif midx==1:
                    yield 2
                else:
                    yield 1
            elif maxx==1:
                if midx==1:
                    yield 2
                else:
                    yield 1
            else:
                yield 0

                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')

##1 1 1
##1   1
##  1 1
##1 1
##1
##  1
##    1
            
