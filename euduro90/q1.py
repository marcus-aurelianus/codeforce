import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,c = list(map(int,input().split()))
        if a>c:
            yield "-1 1"
        elif a==c:
            yield "-1 "+str(b)
        else:
            perprice=c/b
            if perprice>=a:
                yield "1 -1"
            else:
                yield "1 "+str(b)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
