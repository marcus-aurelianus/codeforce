import sys
input = lambda: sys.stdin.readline().rstrip()
N, M, P = map(int, input().split())
A = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
for i, a in enumerate(A):
    if a % P:
        for j, b in enumerate(B):
            if b % P:
                print(i+j)
                exit()
