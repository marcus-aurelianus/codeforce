import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

import math
def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        ans = [i+1 for i in range(2*k-n-1)] + [k-i for i in range(n-k+1)]

        yield " ".join([str(x) for x in ans])
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
# 1 2 3 4 5 4 3 2 1
# 4+6+4+2=16
# 1 2 5 4 3 4 5 2 1
# 7+5+2+2=16
# 1 2 3 5 4 5 3 2 1
# 7+3+4+2=16
# 1 3 2 3 1

# 1 2 3 2 1

