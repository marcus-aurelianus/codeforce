import sys
 
sys.setrecursionlimit(10**5)
 
num = input()
 
n = len(num)
 
ans = 0
mod = 1000000007
##for i in range(n):
##    for j in range(i,n):
##        print(num[:i]+num[j+1:])
##        if (num[:i]+num[j+1:]!=""):
##            ans += int(num[:i]+num[j+1:])
##            ans %= mod
 
#print(ans)
 
tis = [0]*n
 
 
sim = int(num[0])
for i in range(1,n):
    #j = i-1
    #print(i,(i*(i+1))//2*(int(num[i])),num[i])
    tis[i]=((n-i)*(sim)+(i*(i+1))//2*(int(num[i])))
 
    sim = (sim + int(num[i]))
 
ten = [1]
for _ in range(n): ten.append(ten[-1]*10%mod)

for i in range(n):
    ans = (ans + tis[n-1-i]*ten[i]) % mod
print(ans)
        
