import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        trees = []
        for i in range(n):
            tree = input()
            trees.append(tree)
        ans = 0
        for i in range(n):
            for j in range(m):
                if trees[i][j]=='*':
                    ans+=1
                    s,e = j-1,j+1
                    depth = i+1
                    while True:
                        gotIt = True
                        if depth==n:
                            break
                        elif s<0:
                            break
                        elif e>=m:
                            break
                        else:
                            for index in range(s,e+1):
                                if trees[depth][index]=='.':
                                    gotIt=False
                                    break
                        if gotIt:
                            ans+=1
                        else:
                            break
                        s-=1
                        e+=1
                        depth+=1
        yield ans
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
