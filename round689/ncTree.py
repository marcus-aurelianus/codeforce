import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n,m = list(map(int,input().split()))
        trees = []
        for i in range(n):
            tree = list(input())
            trees.append(tree)

        gone = defaultdict(lambda:False)
        bfs = []
        ans=0
        for i in range(n):
            for j in range(m):
                if trees[i][j]=='*':
                    
                    if i==0 or j==0 or j==m-1:
                        bfs.append([i,j])
                        gone[(i,j)]=True
                        ans+=1
                    elif trees[i][j-1]=='.' or trees[i][j+1]=='.' or trees[i-1][j]=='.':
                        bfs.append([i,j])
                        gone[(i,j)]=True
                        ans+=1
        #print(bfs,ans)
        depth=2
        while bfs:
            newbfs = []
            for x,y in bfs:
                #print(x,y)
                if x<n-1 and trees[x+1][y]=='*' and not gone[(x+1,y)]:
                    gone[(x+1,y)]=True
                    newbfs.append([x+1,y])
                    ans+=depth
                if y<m-1 and trees[x][y+1]=='*' and not gone[(x,y+1)]:
                    gone[(x,y+1)]=True
                    newbfs.append([x,y+1])
                    ans+=depth
                if y>0 and trees[x][y-1]=='*' and not gone[(x,y-1)]:
                    gone[(x,y-1)]=True
                    newbfs.append([x,y-1])
                    ans+=depth                    
            #print(ans,newbfs)
            depth+=1
            bfs=newbfs
        yield ans
        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
