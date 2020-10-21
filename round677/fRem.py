import math
from sys import stdin
 
n,m,k = map(int,stdin.readline().split())
 
a = []
for i in range(n):
    tmp = list(map(int,stdin.readline().split()))
    a.append(tmp)
 
maxlis = []
 
for i in range(n):
 
    tdp = [[float("-inf")] * k for i in range(m//2+1)]
    tdp[0][0] = 0
    
    for j in range(m):
        for x in range(len(tdp)-2,-1,-1):
            for y in range(k):
                tdp[x+1][(y+a[i][j])%k] = max(tdp[x+1][(y+a[i][j])%k] , tdp[x][y] + a[i][j])
    
    udp = [float("-inf")] * k
    for x in range(len(tdp)):
        for y in range(k):
            udp[y] = max(udp[y] , tdp[x][y])
 
    maxlis.append(udp)
 
 
dp = maxlis[0]
 
for i in range(1,len(maxlis)):
 
    now = maxlis[i]
    ndp = [float("-inf")] * k
 
    for x in range(k):
        for y in range(k):
            ndp[(x+y)%k] = max(ndp[(x+y)%k] , dp[x]+now[y])
    dp = ndp
 
#print (maxlis)
print (dp[0])
