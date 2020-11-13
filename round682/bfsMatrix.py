import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))

        ans = []
        for i in range(n):
            ans.append(list(map(int,input().split())))
        for i in range(n):
            for j in range(m):
                if ans[i][j]&1 == (i+j)&1:
                    ans[i][j] += 1
           
        for i in range(n):
            yield " ".join([str(x) for x in ans[i]])
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 3 1
# 2 3
# 2 2
