import sys
import math
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def monster():
        n,Am,Ao,spe=map(int,input().split())
        a=list(map(int,input().split()))
        res=0
        spelist=[]
        for i in range(n):
            lefthp=a[i]%(Am+Ao)
            if lefthp<=Am and lefthp!=0:
                res+=1
            else:
                if lefthp==0:
                    hpleft=Am+Ao
                else:
                    hpleft=lefthp
                    
                speneed=math.ceil(hpleft/Am)-1
                #print(hpleft,speneed)
                spelist+=[speneed]
        spelist.sort()
        #print(spelist,res)
        for spell in spelist:
            if spe>=spell:
                res+=1
                spe-=spell
            else:
                break
        yield res
    
            
         
        
            
                    
            
if __name__ == '__main__':

    ans = monster()
    print(*ans,sep='\n')
