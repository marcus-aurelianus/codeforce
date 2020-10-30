import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict

def gift():
    for _ in range(t):
        n = int(input())
        array = sorted(list(map(int,input().split())))

        dp = [[float("inf")] * (2*n+1) for i in range(n+1)]
        dp[0][0] = 0
        
        for i in range(1,n+1):
     
            nt = array[i-1]
     
            for j in range(1,2*n+1):
                for k in range(j):
                    dp[i][j] = min(dp[i][j] , dp[i-1][k] + abs(nt-j))

        yield min(dp[n])

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
