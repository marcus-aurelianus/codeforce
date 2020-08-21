from sys import stdin
import sys
 
n,d,m = map(int,stdin.readline().split())
 
a = list(map(int,stdin.readline().split()))
 
a.sort()
a.reverse()
over = [0]
below = [0]
 
nuse = 0
for i in range(n):
    if a[i] > m:
        over.append(over[-1] + a[i])
    else:
        below.append(below[-1] + a[i])
 
ans = 0
#ans = over[min( len(over)-1 , (n+d) // (d+1) )]
 
print(over,below)
if len(over) == 1:
    print (below[-1])
    sys.exit()
 
#left
for l in range(len(below)):
    r=n-1
    if r < len(over)-1 or (len(over)-1) * (d+1) < r:
        continue
    ans = max(ans , below[l] + over[(r+d)//(d+1)])
 
print (ans)
