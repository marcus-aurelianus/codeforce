import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n,d,m= list(map(int,input().split()))

array = list(map(int,input().split()))
array.sort()

les=[]
big=[]
for i in range(n):
    if array[i]<=m:
        les.append(array[i])
    else:
        big.append(array[i])

res=sum(les)

len1=len(les)
len2=n-len1


s,e=0,len2-2

ans=0
#print(array,big)
while s<len1 and e>=0:
    #print(s,e)

    if (s+d)<=len1:
        sumup=0
        for i in range(s,s+d):
            sumup+=les[i]
        #print(sumup,"sum")
        if sumup<big[e]:
            ans+=(big[e])
            e-=1
            s+=d
        else:
            break
    else:
        break

#print(s,ans)
for i in range(s,len1):
    ans+=les[i]
if len2>=1:
    ans+=big[len2-1]

first=True
while (e>0):
    ans+=big[e]
    if first:
        e-=((d+1)*2)
        first=False
    else:
        e-=(d+1)


print(ans)
