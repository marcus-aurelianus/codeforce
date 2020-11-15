import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math

def gift():
    for _ in range(t):
        n,W = list(map(int,input().split()))
        items = list(map(int,input().split()))

        acum = 0
        seq = []
        ans = False
        for index,ele in enumerate(items):
            if acum+ele<=W:
                acum+=ele
                seq.append(index+1)
            elif ele>=math.ceil(W/2) and ele<=W:
                acum=ele
                seq=[index+1]
            if acum>=math.ceil(W/2) and acum<=W:
                ans = True
                break
        if ans:
            yield len(seq)
            yield " ".join([str(x) for x in seq])
        else:
            yield -1

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            

#1+2
#"{} {} {}".format(maxele,minele,minele)
# 1 2 3 4
# 10 9 8 7

# 1 2 3 4

# 9 2 3 4
# 8 1 3 4
# 7 1 2 4
# 6 1 2 3

# 1 2 3
# 1 3 4
# 3 3 6
# 6 6 6
