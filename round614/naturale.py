import math

def harmo(n):
    return math.log(n)+0.5772156649+1/(2*n)-1/(12*(n*2))

def reach(n) :
    if n==1:
        return 1
    else:
        return 1/n + reach(n-1)
##for i in range(1,1000):
##    print(i,harmo(i)-reach(i),abs(harmo(i)-reach(i))<0.0001)

n = int(input())

if n<=414:
    print(reach(n))
else:
    print(harmo(n))
