import sys
import copy
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

nums=["1110111", "0010010", "1011101", "1011011", "0111010", "1101011", "1101111", "1010010", "1111111", "1111011"]
dic={"1110111":0,"0010010":1, "1011101":2, "1011011":3, "0111010":4, "1101011":5, "1101111":6, "1010010":7, "1111111":8, "1111011":9}
changedic={0: {8: 1}, 1: {3: 3, 4: 2, 7: 1, 8: 5, 9: 4}, 2: {8: 2}, 3: {8: 2, 9: 1}, 4: {8: 3, 9: 2}, 5: {8: 2, 9: 1}, 6: {8: 1}, 7: { 3: 2, 8: 4, 9: 3}, 8: {}, 9: {8: 1}}
n,k = list(map(int,input().split()))
def findnearestbiggestNum(inputnum):
    needk=8
    bestnum=-1
    bestform=None
    for k,v in dic.items():
        counter=0
        tans=True
        for i in range(7):
            inputi=inputnum[i]  
            respecti=k[i]
            if inputi=='1' :
                if respecti=='0':
                    tans=False
                    break
                else:
                    continue
            else:
                if respecti=='1':
                    counter+=1
                else:
                    continue
        if tans:
            if counter<needk:
                needk=counter
                bestnum=v
                bestform=k
            elif counter==needk:
                if v>bestnum:
                    bestnum=v
                    bestform=k
    if bestnum>=0:
        return bestform,bestnum,needk
    else:
        return None
    
tempans=[]
gotit=True
for i in range(n):
    digi=input()
    jojoans=findnearestbiggestNum(digi)
    #print(jojoans)
    if jojoans:
        form,num,needk=jojoans
        
        tempans.append(num)
        k-=needk
    else:
        gotit=False
#print(tempans,k)
anscom=[]
if gotit and k>=0:
    inamo=0
    flag=False
    while inamo<n:
        temp=[]
        if anscom==[]:
            canchange=changedic[tempans[0]]
            
            for ele,tominus in canchange.items():
                respectempk=k
                if respectempk>=tominus:
                    respectempk-=tominus
                    temp.append([[ele],respectempk])
            inamo+=1
            anscom=temp

        else:
            temp=[]
            allcan=True
            #print(anscom)
            for respec in anscom:
                if respec[1]!=0:
                    allcan=False 
                    restemp,resptempk=respec
                  
                    canchange=changedic[tempans[inamo]]
                    #print(canchange)
                    for ele,tominus in canchange.items():
                        #print(ele,tominus,resptempk)
                        copytempk=resptempk
                        copyrestemp=copy.deepcopy(restemp)
                        if copytempk>=tominus:
                            
                            copytempk-=tominus
                            copyrestemp.append(ele)
                            newrespec=[copyrestemp,copytempk]
                            temp.append(newrespec)
                else:
                    restemp,resptempk=respec
                    restemp.append(tempans[inamo])
                    temp.append([restemp,0])
            anscom=temp
            inamo+=1
            #print(temp)
            if allcan:
                break
                
    biggest=0
    #print(anscom)
    for putang in anscom:
        restemp,resptempk=putang
        if resptempk==0:
            biggest=max(biggest,int("".join(str(x) for x in restemp)))
    if biggest==0:
        print("".join(str(x) for x in tempans))
    else:
        print(int(str(biggest)+"".join(str(x) for x in tempans[inamo:])))
else:
    print (-1)
                
