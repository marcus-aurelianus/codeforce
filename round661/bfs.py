import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from collections import defaultdict
def gift():
    for _ in range(t):
        n,maxi=map(int,input().split())
        trees=defaultdict(lambda:[])
        for i in range(n-1):
            node1,node2,v=map(int,input().split())
            trees[node1].append([node2,v])
            trees[node2].append([node1,v])
        bfs=[1]
        branches=[]
        visited=[False]*n
        while bfs:
            newbfs=[]
            for ele in bfs:
                visited[ele-1]=True
                newpoints=trees[ele]
                for point,weight in newpoints:
                    if not visited[point-1]:
                        newbfs.append(point)
                        branches.append(weight)
            bfs=newbfs
        gap=maxi/(n-1)
        branches.sort()
        tochange=[]
        rem=0

        for ele in branches:
            if ele<=gap:
                rem+=(gap-ele)
            else:
                tochange.append(ele)
        if not tochange:
            yield 0
        else:
            nowlen=len(tochange)
            threshold=(gap*nowlen+rem)/nowlen

            ans=0

            for ele in tochange:
                #print(threshold,ans)
                while ele>threshold:
                    ans+=1
                    ele>>=1
                if nowlen>1:
                    threshold=(threshold*(nowlen)-ele)/(nowlen-1)
                    nowlen-=1
            
            yield ans

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
#1 5 4 2 3
