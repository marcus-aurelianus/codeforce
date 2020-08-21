import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())

        d=list(map(int,input().split()))
        interval = []
        end = 2 * n
        while end > 0:
            maxn = 0
            maxi = -1
            for i in range(0, end):
                if maxn < d[i]:
                    maxn = d[i]
                    maxi = i
            interval.append(end - maxi)
            end = maxi
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in interval:
            for j in range(n - 1, -1, -1):
                if dp[j] == 1 and i + j <= n:
                    dp[j + i] = 1
        print(dp,interval)
        if dp[n]==1:
            yield 'YES'
        else:
            yield 'NO'

 


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


