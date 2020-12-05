import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from itertools import permutations
def fx(a, b, c, d):
    return min(b, c) - max(a, d), max(b, c) - min(a, d), abs(b-c)+abs(a-d)
def gift():
    for _ in range(t):
        points = []

        for i in range(4):
            x,y = list(map(int,input().split()))
            points.append([x,y])
            
        ans = float("inf")
        for pp in permutations(list(range(4)), 4):
            (ax, ay), (bx, by), (cx, cy), (dx, dy) = [points[p] for p in pp]
            k1, k2, ll = fx(ax, bx, cx, dx)
            k3, k4, llb = fx(ay, cy, dy, by)
            for k in [k1, k2, k3, k4, 0]:
                if k < 0:
                    continue
                xx = ll + 2*max(k-k2, k1-k, 0)
                yy = llb + 2*max(k-k4, k3-k, 0)
                print(xx,yy)
                ans = min(ans, xx+yy)        
        yield ans               
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
