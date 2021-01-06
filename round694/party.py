import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        assigns = list(map(int,input().split()))
        gifts = list(map(int,input().split()))
        assigns.sort(reverse=True)
        curr = 0
        ans = 0
        for ele in assigns:
            if ele>curr:
                ans+=gifts[curr]
                curr+=1
            else:
                ans+=gifts[ele-1]
        yield ans
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
