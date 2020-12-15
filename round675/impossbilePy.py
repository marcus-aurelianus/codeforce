import sys

num = input()

n = len(num)

ans = 0
md = 1000000007
##for i in range(n):
##    for j in range(i,n):
##        print(num[:i]+num[j+1:])
##        if (num[:i]+num[j+1:]!=""):
##            ans += int(num[:i]+num[j+1:])
##            ans %= mod

#print(ans)



cc = [0]
ten = [1] 
 
for i in range(n+1):
    #j = i-1
    #print(i,(i*(i+1))//2*(int(num[i])),num[i])
    ten.append(ten[-1]*10%md)
    cc.append((cc[-1]+ten[i]*(i+1))%md)
    
 
 
 
for i, a in enumerate(num):
    a=int(a)
    ans += a*(cc[n-i-1]+ten[n-i-1]*i*(i+1)//2)
    ans %= md
print(ans)





