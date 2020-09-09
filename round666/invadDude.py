import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n,r1,r2,r3,d = map(int,input().split())
a = list(map(int,input().split()))
 
dp = [0,float("inf")]
for i in range(1,n+1):
 
    na = a[i-1]
    ndp = [float("inf"),float("inf")]
    c1 = r1*na+r3
    c2 = min(r1*(na+2) , r2+r1)
 
    if i != n:
        ndp[0] =  min( dp[0]+c1 , dp[1]+min(c1,c2) )
        ndp[1] = dp[0] + c2 + 2*d
 
    if i == n:
        print (min(dp[0]+c1,dp[0]+c2+2*d,dp[1]+c2,dp[1]+c1-d) + d*(n-1))
 
    dp = ndp
    
#print(resArray,pipa)
#1 3 2 4
#1 12 8 12
#4 


# 11 10 9 8

# 0 6 5 5
# 6 5 5
# 6 1 1 
# 
