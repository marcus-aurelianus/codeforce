import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n,q = list(map(int,input().split()))


eles = list(map(int,input().split()))

sumE = sum(eles)
for i in range(q):
    t,k = list(map(int,input().split()))    
    if t == 1:
        if eles[k-1] == 0:
            eles[k-1] = 1
            sumE += 1
        else:
            eles[k-1] = 0
            sumE -= 1
    else:
        if k<=sumE:
            print(1)
        else:
            print(0)
