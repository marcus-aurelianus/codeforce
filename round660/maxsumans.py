from sys import stdin
from collections import deque
 
n = int(stdin.readline())
a = list(map(int,stdin.readline().split()))
p = list(map(int,stdin.readline().split()))
 
chnum = [0] * n
for i in range(n):
    if p[i]-1 >= 0:
        chnum[p[i]-1] += 1
 
q = deque([])
for i in range(n):
    if chnum[i] == 0:
        q.append(i)
 
ans = 0
alis = []
end = []
 
while len(q) > 0:
 
    v = q.popleft()
    ans += a[v]
 
    if a[v] >= 0:
        alis.append(v+1)
        if p[v]-1 >= 0:
            chnum[p[v]-1] -= 1
            a[p[v]-1] += a[v]
            if chnum[p[v]-1] == 0:
                q.append(p[v]-1)
    else:
        end.append(v+1)
        if p[v]-1 >= 0:
            chnum[p[v]-1] -= 1
            if chnum[p[v]-1] == 0:
                q.append(p[v]-1)
 
end.reverse()
for i in end:
    alis.append(i)
 
print (ans)
print (*alis)
