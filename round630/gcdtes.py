import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

import math
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
inamo=[2,3,5,7,11,13,17,19,23,29,31]
def gift():
    for _ in range(t):
        n=int(input())
        elements = list(map(int,input().split()))
        res=[]
        used={}
        counter=0
        for ele in elements:
            found=False
            for ina in inamo:
                if ele%ina==0:
                    res.append(ina)

                    inorno=used.get(ina,False)
                    #print(inorno)
                    if not inorno:
                        counter+=1
                        used[ina]=[True,counter]
                    
                    #print(used,ina,ele)
                    found=True
                    break
            if not found:
                res.append(1)
        ans=[]
        totlen=len(used)
        for ele in res:
            if ele==1:
                totlen+=1
                ans.append(totlen)
            else:
                ans.append(used[ele][1])
            
                
        #print(ans)
        yield totlen
        yield " ".join(str(kap) for kap in ans)
        
    
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')

##ele=            
##for i in range(1,1001):
##    found=False
##    for e in ele:
##        
##        if i%e==0:
##            found=True
##            break
##    if not found:
##        print(i,factors(i))
