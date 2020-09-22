import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n = int(input())
arry = list(map(int,input().split()))

arry.sort()

ans = [0]*n

if n%2:
    rangen = n//2 + 1
else:
    rangen = n//2
for i in range(rangen):
    if n//2 + i < n:
        ans[i*2] = arry[n//2 + i]
    if i * 2 + 1 < n:
        ans[i*2+1] = arry[i]

res = 0

for i in range(1,n-1):
    if ans[i]<ans[i-1] and ans[i]<ans[i+1]:
        res+=1
print(res)
print(" ".join([str(x) for x in ans]))

#"{} {} {}".format(maxele,minele,minele)
# 4 1 3 2 5 
