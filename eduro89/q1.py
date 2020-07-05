import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b = list(map(int,input().split()))
        c=min(a,b)
        d=max(a,b)
        
        if d>=2*c:
            yield c
        else:
            yield (c+d)//3


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')


# 2x+y<a
# 2y+x<b

#3x+3y<a+b
#x<
            
