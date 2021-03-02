import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

def gift():
    for _ in range(t):
        n = int(input())
        ans = list(range(2,n+1))+[1]
        dingdong = 0
        for i in range(1,n):
            dingdong+=i**2
        yield dingdong
        yield " ".join([str(x) for x in ans])
        yield n-1
        for i in range(n-1):
            yield "{} {}".format(i+1,n)
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])

# 2 3 4 1
# 2 4 3 1
# 4 2 3 1
# 1 2 3 4

# 1 3 4 2
# 1 2 4 3


# 1 4
# 2 4
# 3 4
