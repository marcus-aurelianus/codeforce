import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

N, K = map(int, input().split())
S = [1 if a == "R" else 0 for a in input()]
 
t = 0
a = 0
for s in S:
    if s:
        a += 1
    else:
        t += a

if K>t:
    print(-1)
    exit()


X=[]
while True:
    Y=[i for i in range(N-1) if S[i] and not S[i+1]]
    if not len(Y): break
    X.append(Y)
    nS = [0] * N
    i = N - 1
    while i >= 0:
        if S[i-1] and not S[i] and i:
            nS[i] = 1
            i -= 2
        elif S[i]:
            nS[i] = 1
            i -= 1
        else:
            i -= 1
    S = nS
u = len(X)
if K < u:
    print(-1)
    exit()
p1 = lambda x: [y+1 for y in x]
st = lambda x: " ".join(map(str, x))
ANS = []
K -= u
i = 0
#print(X,K)
for x in X:
    for j, xx in enumerate(x):
        if K:
            ANS.append(st([1, xx + 1]))
            if j < len(x) - 1: K -= 1
        else:
            ANS.append(st([len(x) - j] + p1(x[j:])))
            break
 
strANS = "\n".join(ANS)
print(strANS)

            

