import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


n,k = list(map(int,input().split()))

citydis={}

for i in range(n-1):
    cityf,cityt = list(map(int,input().split()))
    desf=citydis.get(cityf,[])
    dest=citydis.get(cityt,[])
    desf.append(cityt)
    dest.append(cityf)
    citydis[cityf]=desf
    citydis[cityt]=dest

initdis={1:0}
dis=1
nodes=[1]
snode=[]
while True:
    replacenode=[]
    for node in nodes:
        temp=citydis[node]
        for tempnode in temp:
            wentorno=initdis.get(tempnode,False)
            if not wentorno and tempnode!=1:
                initdis[tempnode]=dis
                replacenode.append(tempnode)
                cityto=citydis[tempnode]
                #print(citydis,tempnode,cityto)
                if len(cityto)==1:
                    snode.append(tempnode)
    dis+=1
    if not replacenode:
        break
    nodes=replacenode
ansnode={}
#print(citydis,snode,initdis)

initdisitem=list(initdis.items())

initdisitem.sort(key=lambda x:-x[1])

for nodeinamo in initdisitem:
    node=nodeinamo[0]
    temp=citydis[node]
    bitchnode=citydis[node]

    bitches=0
    for itsnode in bitchnode:

        if initdis[itsnode]>initdis[node]:
       
            bitches+=(ansnode[itsnode][1]+1)
   
        
    ansnode[node]=[initdis[node],bitches] 

anss=list(ansnode.items())


anss.sort(key=lambda x:-x[1][0]+x[1][1])

ans=0
for i in range(k):
    ans+=((anss[i][1][0]-anss[i][1][1]))
print(ans)
