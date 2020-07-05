di='cocefordes'


ans=[]
n=len(di)
for i in range(n):
    temp=0
    for j in range(n):
        if ord(di[j])>ord(di[i]):
            temp+=abs(j-i)
    ans.append(temp)
print(ans)
