import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        a,b,c,d = list(map(int,input().split()))
        yield max(a+b,c+d)

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
