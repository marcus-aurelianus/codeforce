import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n=int(input())

trees={}
for i in range(n-1):
    t1,t2 = list(map(int,input().split()))
    t1t,t1f=trees.get(t1,[[],0])
    t1t.append(t2)
    t1f+=1
    trees[t1]=[t1t,t1f]
    t2t,t2f=trees.get(t2,[[],0])
    t2t.append(t1)
    t2f+=1
    trees[t2]=[t2t,t2f]
#print(trees)
itemrino=list(trees.items())
itemrino.sort(key=lambda x:x[1][1])


singlenode=list(filter(lambda x:x[1][1]==1,itemrino))
toquery=list(map(lambda x:x[0],singlenode))
#multinode=list(filter(lambda x:x[1][1]!=1,itemrino))
#multoquery=list(map(lambda x:x[0],multinode))
#print(toquery)

queried={}
while True:
    n=len(toquery)
    if n<2:
        break
    if n%2==0:
        toadd=[]
    else:
        toadd=[toquery[-1]]
    for i in range(n//2):
        query = "?"
        node1,node2=toquery[i*2],toquery[i*2+1]
        if node1 in toadd:
            if node2 not in toadd:
                toadd.append(node2)
            continue
        elif node2 in toadd:
            if node1 not in toadd:
                toadd.append(node1)
            continue            
        else:     
            
            query += " "
            query += str(node1)
            query += " "
            query += str(node2)
            print (query, flush = True)
            
            top=int(input())
            queried[node1]=top
            queried[node2]=top
            if top ==node1 or top==node2:
                toquery=[top]
                break
            if top not in toadd:
                toadd.append(top)
        
            
    if n==2:
        toquery=[top]
    else:
        toquery=toadd
print ("!" , toquery[-1] , flush = True)
 
##for i in range(k+1):
## 
##    query = "?"
##    for j in range(k+1):
##        if i != j:
##            query += " "
##            query += str(q[j])
## 
##    print (query, flush = True)
## 
##    pos,num = map(int,input().split())
##    if num not in exist:
##        exist.append(num)
##        dic[num] = 1
##    else:
##        dic[num] += 1
## 
##exist.sort()
##print ("!" , dic[exist[-1]] , flush = True)
