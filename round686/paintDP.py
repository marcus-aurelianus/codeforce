import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        
        n,k = list(map(int,input().split()))
        c = list(map(int,input().split()))
        fans = float("inf")
        for i in range(1,101):
            j = 0
            temans = 0
            while j<n:
                if c[j]!=i:
                    temans+=1
                    j+=k
                else:
                    j+=1
            fans = min(fans,temans)
        yield fans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
#####
###x#
#####
