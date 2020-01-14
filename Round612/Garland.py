N = int(input())
A = [int(a) for a in input().split()]
M = A.count(0)
A2 = [a%2 for a in A]
O = A2.count(1)
E = N - M - O
O = (N+1)//2 - O
E = N//2 - E
C = [M]
for a in A:
    C.append(C[-1] - (a == 0))
 
X = [[999] * (N+2) for _ in range(N)]
Y = [[999] * (N+2) for _ in range(N)]
if A[0] % 2:
    X[0][O] = 0
elif A[0]:
    Y[0][O] = 0
else:
    if O: X[0][O-1] = 0
    if E: Y[0][O] = 0
print(X,Y)
for i in range(1, N):
    for j in range(N+1):
        if A[i] % 2:
            X[i][j] = min(X[i-1][j], Y[i-1][j] + 1)
        elif A[i]:
            Y[i][j] = min(X[i-1][j] + 1, Y[i-1][j])
        else:
            X[i][j] = min(X[i-1][j+1], Y[i-1][j+1] + 1)
            Y[i][j] = min(X[i-1][j] + 1, Y[i-1][j])
print("")
for i in range(N):
    print(X[i],Y[i])        
print(min(X[N-1][0], Y[N-1][0]))
