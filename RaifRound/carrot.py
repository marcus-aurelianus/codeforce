from heapq import *

n,k=map(int,input().split(" "))

#idea cut the longest every time
def val(l,nums):
    unit=l//nums
    extra=l-unit*nums
    return (nums-extra)*unit*unit+extra*(unit+1)*(unit+1)
    
pq=[]
arr=list(map(int,input().split(" ")))

total=0
for x in range(n):
    total+=arr[x]*arr[x]
    heappush(pq,(-val(arr[x],1)+val(arr[x],2),arr[x],2))

for x in range(k-n):
    temp=heappop(pq)
    total+=temp[0]
    a,b=temp[1],temp[2]
    heappush(pq,(-val(a,b)+val(a,b+1),a,b+1))

print(total)
