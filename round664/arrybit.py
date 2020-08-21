n,m=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split())) 
ans=-1
for mask in range(2**9):
    bol=True
    for i in  arr:
        b=False
        for j in brr:
            if (~mask)&(i&j)==0:
                b=True
                break
        if not b:
            bol=False
    if bol:
        ans=mask
        break
print(ans)
 
