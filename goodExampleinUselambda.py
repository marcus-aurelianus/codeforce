import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda x, y, z: (x-y) ** 2 + (y-z) ** 2 + (z-x) ** 2
f = lambda i, j, k: g(A[i], B[j], C[k])
 
T = int(input())
for _ in range(T):
    na, nb, nc = map(int, input().split())
    na, nb, nc = na-1, nb-1, nc-1
    A = sorted([int(a) for a in input().split()])
    B = sorted([int(a) for a in input().split()])
    C = sorted([int(a) for a in input().split()])
    i, j, k = 0, 0, 0
    mi = f(i, j, k)
    n = na + nb + nc
    while n:
        a = f(i+1, j, k) if i < na else 1 << 100
        b = f(i, j+1, k) if j < nb else 1 << 100
        c = f(i, j, k+1) if k < nc else 1 << 100
        if b > a < c:
            i += 1
        elif b < c:
            j += 1
        else:
            k += 1
        mi = min(mi, f(i, j, k))
        n -= 1
    print(mi)
