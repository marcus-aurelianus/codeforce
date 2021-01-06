import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
def gift():
    for _ in range(t):
        n,x = list(map(int,input().split()))
        arry = list(map(int,input().split()))
        maxR = 0
        for ele in arry:
            maxR += math.ceil(ele/x)

        yield "{} {}".format(math.ceil(sum(arry)/x),maxR)

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
