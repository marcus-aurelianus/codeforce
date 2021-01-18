import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

import math
def gift():
    for _ in range(t):
        s = list(input())
        r = list(input())
        n = len(s)
        m = len(r)
        lcm = n*m//math.gcd(n,m)
        news = s*(lcm//n)
        newr = r*(lcm//m)
        if news==newr:
            yield "".join([str(x) for x in news])
        else:
            yield -1
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])

# 1 2 3 5 4 5 3 2 1
