import sys
input = sys.stdin.readline
 
mod=10**9+7
ANS=[0,0,0,4,4]
HEAD=[0,0,0,1,0]
for i in range(2*10**6):
    if HEAD[-1]==0 and HEAD[-2]==0:
        ANS.append((ANS[-1]+ANS[-2]*2+4)%mod)
        HEAD.append(1)
    else:
        ANS.append((ANS[-1]+ANS[-2]*2)%mod)
        HEAD.append(0)

 
t=int(input())
for tests in range(t):
    n=int(input())
    print(ANS[n])
