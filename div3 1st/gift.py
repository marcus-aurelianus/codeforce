import copy
if __name__ == '__main__':
    n= int(input())
    gift = {x+1:0 for x,i in enumerate(range(1,n+1))}
    #input().split()
    giftMissing=list(range(1,n+1))
    while 0 in gift.values():
        
        missingDict={}
        while True:
            for k,v in gift.items():
                if v==0:
                    missingDict[k]=giftMissing
                elif v in giftMissing:
                    giftMissing.remove(v)
            #print(missingDict)
            kToDel=[]
        
            for k,v in missingDict.items():
                new_v=copy.deepcopy(v)
                if k in v:
                    new_v.remove(k)
                    missingDict[k]=new_v
                if len(new_v)==1:
                    gift[k]=new_v[0]
                    kToDel.append(k)
            if kToDel:
                for key in kToDel:
                    del missingDict[key]
            else:
                break
            #print(missingDict,gift)
        if missingDict:
            lenV=list(map(len,missingDict.items()))
            #print(lenV)
            minlenV=min(lenV)
            minlenVindex=lenV.index(minlenV)
            if minlenV>1:
                key=list(missingDict.keys())[minlenVindex]
                val=missingDict[key][0]
                gift[key]=val
        else:
            break
    #print(gift)  
    print(" ".join(str(x) for x in gift.values()))
    
    

