from collections import defaultdict 
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


class Graph(): 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices 
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def isCyclicUtil(self, v, visited, recStack): 
  
        # Mark current node as visited and  
        # adds to recursion stack 
        visited[v] = True
        recStack[v] = True
  
        # Recur for all neighbours 
        # if any neighbour is visited and in  
        # recStack then graph is cyclic 
        for neighbour in self.graph[v]: 
            if visited[neighbour] == False: 
                if self.isCyclicUtil(neighbour, visited, recStack) == True: 
                    return True
            elif recStack[neighbour] == True: 
                return True
  
        # The node needs to be poped from  
        # recursion stack before function ends 
        recStack[v] = False
        return False
  
    # Returns true if graph is cyclic else false 
    def isCyclic(self): 
        visited = [False] * self.V 
        recStack = [False] * self.V 
        for node in range(self.V): 
            if visited[node] == False: 
                if self.isCyclicUtil(node,visited,recStack) == True: 
                    return True
        return False

haveit={}
n,m=list(map(int,input().split()))
g = Graph(5)
for i in range(m):
    p1,p2=list(map(int,input().split()))
    g.addEdge(p1-1, p2-1)
    diulei=haveit.get(p2-1,[])
    diulei.append(p1-1)
    haveit[p2-1]=diulei
if g.isCyclic(): 
    print (-1)
else :
    ans=""
    count=0
    for i in range(n):
        dingding=g.graph.get(i,[])
        papa=haveit.get(i,[])
        if len(dingding)<=1 and not papa:
            ans+="A"
            count+=1
        else:
            ans+="E"
    print(count)
    print (ans)
