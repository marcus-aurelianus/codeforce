import sys
 
sys.setrecursionlimit(10**5)
int1 = lambda x: int(x)-1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def BI(): return sys.stdin.readline().rstrip()
def SI(): return sys.stdin.readline().rstrip().decode()
 
inf=10**9
def solve():
    l=inf
    r=0
    for a in aa:
        l=min(l,a-r)
        r=a-l
        if l<0 or r<0:return "NO"
    return "YES"
 
for _ in range(II()):
    n=II()
    aa=LI()
    print(solve())
