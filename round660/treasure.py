import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n=int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

dic1={}
dic2={}

dicdef=[]
for i in range(n):
    if b[i]==-1 or b[i]==i+1:
        dicdef.append(i+1)
    else:
        if a[i]>=0:
        
            lis1=dic1.get(b[i],[])
            lis1.append(i+1)
            dic1[b[i]]=lis1
        else:
            lis2=dic2.get(b[i],[])
            lis2.append(i+1)
            dic2[b[i]]=lis2

visited=[False]*n

ansarry=[]

deptharr={}
def dfs(v,visited,temp,depth):
    if depth!=0:
        visited[v-1] = True
        temp.append(v)
    if dic1.get(v,False):
        for i in dic1[v]:
            if visited[i-1]==False:
                dfs(i,visited,temp,depth+1)
 
for key in dic1:
    temp=[]
    dfs(key,visited,temp,0)
    temp=temp[::-1]
    ansarry.extend(temp)


depthitem=list(deptharr.items())
depthitem.sort(key=lambda x:-x[1])

for ele,depth in depthitem:
    ansarry.append(ele)
    



bfs=list(dic2.keys())

while bfs:
    temp=[]
    for ele in bfs:
        if visited[ele-1] == False:
            ansarry.append(ele)
            visited[ele-1] = True
        if dic2.get(ele,False):
            temp.extend(dic2[ele])
    bfs=temp
        
for i in range(n):
    if not visited[i]:
        ansarry.append(i+1)
ans=0


for ele in ansarry:
    ans+=a[ele-1]
    if b[ele-1]!=-1:
        a[b[ele-1]-1]+=a[ele-1]
                
print(ans)
print(" ".join(str(x) for x in ansarry))
            


#"{} {} {}".format(maxele,minele,minele)
