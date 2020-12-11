import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
n,m=500,500
trees=[]
for i in range(n):
    trees.append(['*']*500)
def gift(trees):
    ans = 0
    for i in range(n):
        for j in range(m):
            if (i%50==0 and j%50==0):
                print(i,j)
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
    return ans

print(gift(trees))

#"{} {} {}".format(maxele,minele,minele)
