n= int(input())
 
kappa,nmb = 0, 0
 
bras=input()
for i in range(n):
    if bras[i]=="(":
        kappa+=1
    else:
        kappa-=1
    nmb=min(nmb,kappa)
print("YES")if nmb>=-1 and kappa==0 else print("NO")
