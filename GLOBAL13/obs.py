import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,u,v = list(map(int,input().split()))
        obs = list(map(int,input().split()))
        adj = False
        passable = False
        for i in range(n-1):
            if obs[i] == obs[i+1]:
                continue
            elif abs(obs[i] - obs[i+1]) == 1:
                adj = True
                continue
            else:
                passable = True
                break
        if passable:
            yield 0
        elif adj:
            yield min(u,v)
        else:
            yield min(u + v, 2 * v)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])
