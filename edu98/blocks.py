import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        bricks = list(map(int,input().split()))
        ans = max(bricks)*(n-1)-sum(bricks)
        if ans<0:
            yield ans%(n-1)
        else:
            yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
