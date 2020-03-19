N = int(input())
X = [0] * N
Y = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(int, input().split())
    X[u-1] += 1
    X[v-1] += 1
    Y[u-1].append(v-1)
    Y[v-1].append(u-1)
 
def query(u, v):
    print("?", u+1, v+1)
    return int(input()) - 1
def chk():
    for i in range(N):
        if X[i] == 1:
            for j in range(i+1, N):
                if X[j] == 1:
                    a = query(i, j)
                    if a == i or a == j:
                        print("!", a+1)
                        return 0
                    for u in Y[i] + Y[j]:
                        X[u] -= 1
                    X[i] = -1
                    X[j] = -1
                    return 1
    
    for i in range(N):
        if X[i] == 0:
            print("!", i+1)
            return 0
    
while chk():
    pass
