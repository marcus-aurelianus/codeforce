if __name__ == '__main__':
    n= int(input())
    house = [int(x) for x in input().split()]
    house.sort()
    dict1={}
    for ppl in house:
        freq=dict1.get(ppl,0)+1
        dict1[ppl]=freq
    maxres={}
    minres={}
    for key,var in dict1.items():
        freqp1=dict1.get(key+1,0)
        freqm1=dict1.get(key-1,0)
        freqp2=dict1.get(key+2,0)
        keyinMinresp1=minres.get(key+1,False)
        keyinMinre=minres.get(key,False)
        keyinMinresm1=minres.get(key-1,False)
        if not keyinMinresp1 and not keyinMinre and not keyinMinresm1:
            if freqp1>0 or freqp2>0:
                if not keyinMinresp1:
                    minres[key+1]=True 
            else:
                minres[key]=True
        keyinMaxresp1=maxres.get(key-1,False)
        keyinMaxresm1=maxres.get(key+1,False)
        keyinMax=maxres.get(key,False)
        if var==2:
            
            if not keyinMaxresp1:
                maxres[key-1]=True
                if not keyinMax:
                    maxres[key]=True 
            else:
                if not keyinMax:
                    maxres[key]=True
                if not keyinMaxresm1:
                    maxres[key+1]=True
        if var==1:
            if not keyinMaxresp1:
                maxres[key-1]=True
            elif not keyinMax:
                maxres[key]=True
            elif not keyinMaxresm1:
                maxres[key+1]=True
        if var>=3:
            if not keyinMaxresp1:
                maxres[key-1]=True
            if not keyinMax:
                maxres[key]=True
            if not keyinMaxresm1:
                maxres[key+1]=True
    print(len(minres),len(maxres))
