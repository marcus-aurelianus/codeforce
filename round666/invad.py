import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n, r1, r2, r3, d = list(map(int,input().split()))      
array = list(map(int,input().split()))

resArray = []

for i in range(n):
    resArray.append(array[i]*r1+r3)

pipa = [False]*n
for i in range(n):
    if i == n-1:
        if r2+r1+2*d<resArray[i]:
            pipa[i]=True
    else:
        if r2+r1+d<resArray[i]:
            pipa[i]=True

ans = 0 
for i in range(n):
    #print(ans)
    if i==n-1:
        dis = 0
    else:
        dis = d
        
    if pipa[i]:
        ans += r2 + r1 + d + dis
    else:
        ans += (resArray[i] + dis)
    #print(i,ans,resArray[i],d)
print(ans)
#print(resArray,pipa)
#1 3 2 4
#1 12 8 12
#4 


# 11 10 9 8

# 0 6 5 5
# 6 5 5
# 6 1 1 
# 
