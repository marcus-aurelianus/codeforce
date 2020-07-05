import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        arry = list(map(int,input().split()))
        pma=[0]*(n+1)
        jingcai=True
        for i in range(n):
            pma[arry[i]]+=1
            if i>0:
                if arry[i]<arry[i-1]:
                    jingcai=False   
        if jingcai:
            yield 0
            yield ""
        else:
            s=0
            ansstk=[]
            print(pma)
            while s<=n:
                if pma[s]==0:

                    if s==n:
                        ansstk.append(s)
                    else:
                        ansstk.append(s+1)
                    pma[s]+=1
                    if s==n:
                        datapoint=arry[s-1]
                    else:
                        datapoint=arry[s]

                    pma[datapoint]-=1

                    
                    if pma[datapoint]==0:
                        recurcheckpoint=datapoint
                        print(recurcheckpoint,s,pma,ansstk)
                        adi={}
                        while pma[recurcheckpoint]==0:
                            if recurcheckpoint==n:
                                break
                            pma[recurcheckpoint]+=1
                            print('apoint',recurcheckpoint,arry[recurcheckpoint],ansstk)
                            piu=adi.get(recurcheckpoint,False)
                            if piu:
                                break
                            adi[recurcheckpoint]=True
                            pma[arry[recurcheckpoint]]-=1
                            ansstk.append(recurcheckpoint+1)
                            recurcheckpoint=arry[recurcheckpoint]
                s+=1
            yield len(ansstk)
            yield " ".join(str(x) for x in ansstk)
        


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
#2 1 0



#3 2 1
    
#2 1 3
#[0,0,0,0,0,0]
#[0,7,2,1,3,7,7]
#[0,7,2,1,4,7,7]   
#[0,7,2,3,4,7,7]

   
    
#[0,1,2,3,4,7,7] 
#[0,1,2,3,4,5,7]


#[1,1,0,2,0,0,0,2]
# 2 4 3 1 5   
