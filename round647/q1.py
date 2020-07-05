import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
def gift():
    for _ in range(t):
        a,b = list(map(int,input().split()))
        if a==b:
            yield 0
        else:
            if a>b:
                c=a//b
                d=a%b
            else:
                c=b//a
                d=b%a
            if d:
                yield -1
            else:
                dude=math.log(c,2)
                revdude=2**int(dude)
                #print(dude,revdude)
                if abs(c-revdude)<=0.1**10:
                    e=math.log(c,8)
                    d=8**int(e)
                    #print(d,c,e)
                    if abs(d-c)<0.1**10:
                        yield int(e)
                    else:
                        yield int(e)+1
                else:
                    yield -1
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
