n,m = map(int,input().split())
 
k = [1]
 
for i in range(n):
    i += 1
    k.append(k[-1] * i%m)
ans = 0
for i in range(n):
 
    ans += (n-i) * k[i+1] * k[n-i]
    ans %= m
 
print (ans)
