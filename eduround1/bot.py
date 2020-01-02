import sys
mod=998244353 
# print((2*pow(5,mod-2,mod))%mod)
 
def inv(k):
    return pow(k,mod-2,mod)
    
 
# exit()
d={}
k={}
 
n=int(input())
ans=0
l=[0]*(n)
for _ in range(n):
    d[_]=list(map(int,sys.stdin.readline().split()))
    for i in d[_][1:]:
        k[i]=k.get(i,0) + 1
# print(k)
for  i in range(n):
    for j in d[i][1:]:
        # print(d[i][0],n-k[j])
        ans+=(inv((d[i][0]))*(n-k[j]))%mod
        ans%=mod
        # print(ans)
ans*=inv(n)
 
ans%=mod
ans*=inv(n)
 
ans%=mod
if ans==0:
    print(1)
    exit()
print((mod-ans + 1)%mod)
