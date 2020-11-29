import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n,m,i,j = list(map(int,input().split()))
        yield max((abs(i-1)+abs(j-1)),(abs(n-i)+abs(j-m)),
                  (abs(i-1)+abs(j-m)),(abs(n-i)+abs(j-1)))

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
#####
###x#
#####
