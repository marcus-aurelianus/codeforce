import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n = int(input())
        a1 = list(map(int,input().split()))
        m = int(input())
        b1 = list(map(int,input().split()))

        currMax = 0
        curr = 0 
        for i in range(n):
            curr+=a1[i]
            currMax=max(currMax,curr)

        currMaxB = 0
        currB = 0             
        for i in range(m):
            currB+=b1[i]
            currMaxB=max(currMaxB,currB)
        yield currMax+currMaxB

        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
