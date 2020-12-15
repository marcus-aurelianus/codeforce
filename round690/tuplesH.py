import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import deque
mod = 10**9+7
def modfac(n, MOD):
 
    f = 1
    factorials = [1]
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        factorials.append(f)
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return factorials, invs
fac,inv = modfac(300000,mod)

def modnCr(n,r,mod,fac,inv):
    if n < r:
        return 0
    return fac[n] * inv[n-r] * inv[r] % mod

def gift():
    for _ in range(t):
        n,m,k = list(map(int,input().split()))
        a = list(map(int,input().split()))
        a.sort()

        q = deque([])
        ans = 0

        for i in range(n):
            na = a[i]
            while len(q)>0 and q[0]<na-k:
                q.popleft()
            ans += modnCr(len(q),m-1,mod,fac,inv)
            ans %= mod

            q.append(na)
        yield ans


                    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
    
# 5 1 2 4 5 1 6 4 2
