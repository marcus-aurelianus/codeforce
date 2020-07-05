lst=[1,2,0]


n=len(lst)
res=n+1
for i in range(n):
    res+=((n-i-1)*(lst[i])+lst[i])
print(res)
