import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
n=int(input())


class Node:
    def __init__(self,value):
        self.val=value
        self.prev1=None
        self.next1=None
    def setprev(self,obj):
        self.prev1=obj
    def setnext(self,obj):
        self.next1=obj
    def findshortestlentoNode(self,val):
        if val==self.val:
            return 0
        else:
            dis=1
            prevnode,nextnode=self.prev1,self.next1
            while True:
                if prevnode!=None:
                    if prevnode.val==val:
                        return dis
                    else:
                        prevnode=prevnode.prev1
                if nextnode!=None:
                    if nextnode.val==val:
                        return dis
                    else:
                        nextnode=nextnode.next1
                dis+=1
                
                    
                    
Nodes=[]
for i in range(n):
    nodeinamo=Node(i+1)
    Nodes.append(nodeinamo)
for i in range(n-1):
    prevnodeval,nextnodeval=map(int,input().split())
    prevnode=Nodes[prevnodeval-1]
    nextnode=Nodes[nextnodeval-1]
    prevnode.setnext(nextnode)
    nextnode.setprev(prevnode)

queries=int(input())
for _ in range(queries):
    x,y,a,b,k=map(int,input().split())
    #print(x,y)
    currdis=Nodes[a-1].findshortestlentoNode(b)
    #print(currdis)
    dis1=Nodes[a-1].findshortestlentoNode(x)
    #print(dis1)
    dis2=Nodes[b-1].findshortestlentoNode(y)
    disinamo=dis1+dis2+1
    #print(currdis,disinamo)
    remain=k
    ans=False

    if currdis!=0:
        if k%currdis==0:
            ans=True
        else:
            remain=k%currdis
    if ans:
        print('YES')
    else:
        #print(remain)
        if remain%disinamo==0:
            print('YES')
        else:
            print('NO')
            


#print(Nodes[2].findshortestlentoNode(5))
