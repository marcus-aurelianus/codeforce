import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        ans = []
        for i in range(n):
            ans.append(list(map(int,input().split())))

        absVal = []
        minusCount = 0
        gotZ = False
        for i in range(n):
            for j in range(m):
                if ans[i][j]<0:
                    minusCount+=1
                elif ans[i][j]==0:
                    gotZ = True
                absVal.append(abs(ans[i][j]))
                
        if gotZ:
            yield sum(absVal)
        else:
            absVal.sort()
            #print(minusCount)
            if minusCount%2==0:
                yield sum(absVal)
            else:
                yield sum(absVal[1:])-sum(absVal[:1])

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
