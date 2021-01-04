
lst = [7,1]
n=len(lst)

ans = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            ans = (ans+(lst[i]&lst[j])*(lst[j]|lst[k]))%(10**9+7)


print(ans)
