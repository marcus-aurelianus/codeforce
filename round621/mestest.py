
# Using itertools.combinations() 
from itertools import combinations 
string="egefgfeegf"

allsub=[''.join(l) for i in range(len(string)) for l in combinations(string, i+1)]
allsub=list(set(allsub))
allsub.sort()

print(allsub)
def checklst(lst):
    n=len(lst)
    if n==1:
        return True
    templen=lst[1]-lst[0]
    for i in range(n-2):
        if lst[i+2]-lst[i+1]!=templen:
            return False
    return True

dis={}
for i in range(len(string)):
    ele=string[i]
    if ele not in dis:
        dis[ele]=[i]
    else:
        dis[ele]+=[i]
#print(dis)

result=[]
dud=[]
for sub in allsub:
    tempres=[]
    for element in sub:
        temp=[]
        if tempres==[]:
            for iniele in dis[element]:
                tempres.append([iniele])
        else:
            
            for currele in tempres:

                for disele in dis[element]:
                    if disele>currele[-1] and len(currele)<len(sub):
                        smalltemp=currele.copy()
                        smalltemp.append(disele)
                        temp.append(smalltemp)
            tempres=temp
    count=0
    #print(sub,tempres)
    for ina in tempres:
        if checklst(ina):
            count+=1
    #print(sub,count)      
        
    result.append([sub,count])
    dud.append([sub,tempres])

result.sort(key=lambda x:x[1])
print(result)
                
