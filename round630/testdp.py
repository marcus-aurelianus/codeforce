inamo1=[[7,3,1],[4,3,2],[4,7,3]]
inamo=[[262144-1,131072-1,1],[131072,131072-1,1],[131072,262144-1,131072-1]]

n,m=len(inamo),len(inamo[0])
dp=[]
for i in range(n):
    dp.append([0]*m)
dp[0][0]=inamo[0][0]
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            continue
        else:
            if i==0:
                dp[i][j]=max(dp[i][j],dp[i][j-1]&inamo[i][j])
            elif j==0:
                dp[i][j]=max(dp[i][j],dp[i-1][j]&inamo[i][j])
            else:
                dp[i][j]=max(dp[i][j-1]&inamo[i][j],dp[i-1][j]&inamo[i][j])
print(dp)           
print(dp[n-1][m-1])


