import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,c,d = list(map(int,input().split()))
        x,y,x1,y1,x2,y2 = list(map(int,input().split()))
        endx=x+(b-a)
        endy=y+(d-c)
        if x1==x2 and (a!=0 or b!=0):
            yield "NO"
        elif y1==y2 and (c!=0 or d!=0):
            yield "NO"
        else:
            if x1<=endx<=x2 and y1<=endy<=y2:
                yield "YES"
            else:
                yield "NO"
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
