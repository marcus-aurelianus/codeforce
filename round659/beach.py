t = int(input())
for _ in range(t):
    n, k, l = list(map(int, input().split()))
    dps = list(map(int, input().split()))
    base = -1
    safe = False
    r_old = 1
    for i in range(n):
        r = l-dps[i]
        if r < 0:
            print("No")
            break
        if r >=k:
            r_old = k
            continue
        r_old = min(r_old-1, r)
        if r_old <= 0 and (dps[i]-r_old)>l:
            print("No")
            break
    else:
        print("Yes")
