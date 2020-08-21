import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        arry = list(map(int,input().split()))
        if (arry[0]+arry[1]<=arry[n-1]):
            yield "{} {}  {}".format(1,2,n)
        else:
            yield -1
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
