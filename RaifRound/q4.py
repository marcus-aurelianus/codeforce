def die():
    print(-1)
    exit(0)
 
ones = []
ans = []
H = 1
lastThree = (-1,-1)
 
n = int(input())
arr = list(map(int,input().split(" ")))
 
for i in range(n-1, -1, -1):
    if arr[i] == 0:
        continue
    elif arr[i] == 1:
        ones.append((i,H))
        ans.append((i,H))
        H += 1
    elif arr[i] == 2:
        if len(ones) == 0:
            die()
        T = ones[-1]
        ones.pop()
        ans.append((i, T[1]))
        lastThree = (i,T[1])
    elif arr[i] == 3:
        if lastThree[0] == -1:
            if len(ones) == 0:
                die()
            else:
                lastThree = ones[-1]
                ones.pop()
        ans.append((i, H))
        ans.append((lastThree[0], H))
        lastThree = (i,H)
        H += 1
 
print(len(ans))
for ii in ans:
    print(n-ii[1] + 1, end = ' ')
    print(ii[0] + 1)
