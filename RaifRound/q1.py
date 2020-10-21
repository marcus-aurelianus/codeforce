import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,c,d= list(map(int,input().split()))
        if c==a:
            yield abs(d-b)
        elif d==b:
            yield abs(c-a)
        else:
            yield abs(c-a)+abs(d-b)+2

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
