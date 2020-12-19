import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
import copy

n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
            
mina = min(a)

ans = []

arry = []
dupVar = []
copya = copy.deepcopy(a)
copya.sort()
for i in range(n-1):
    if copya[i+1]-copya[i]!=0:
        arry.append(copya[i+1]-copya[i])
    else:
        dupVar.append(copya[i+1])
if len(arry)==0:
    for i in range(m):
        ans.append(mina + b[i])
else:
    currMin = min(arry)
    for ele in arry:
        if currMin%ele==0 or ele%currMin==0:
            currMin=min(currMin,ele)
        else:
            currMin = math.gcd(currMin,ele)
        if currMin ==1:
            break

    if currMin==1:
        for i in range(m):
            ans.append(1)
    else:
        for i in range(m):
            if currMin%(mina+b[i])==0:
                ans.append(mina+b[i])
            elif (mina+b[i])%(currMin)==0:
                ans.append(currMin)
            else:
                ans.append(1)       

print(" ".join([str(x) for x in ans]))

#"{} {} {}".format(maxele,minele,minele)
# 997 1000 1001



