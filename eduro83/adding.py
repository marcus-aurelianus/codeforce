import sys
import math
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

#print(math.log(9999999999999999,100))

def getit(num,base):
    res=[]
    while True:
        if num==0:
            return res
        else:
            
            lognum=int(math.log(num,base))
            revnorm=base**lognum
            revnormp1=base**(lognum+1)
            revnormm1=base**(lognum-1)
            #print(res,lognum,revnorm,num,revnormp1)

            if lognum==0 and revnorm!=num  or revnormp1!=revnormp1:
                #print('con1')
                return False  
            elif revnorm==num:
                #print('con2')
                num=0
                res.append(lognum)
            elif revnormp1==num:
                #print('con3')
                num=0
                res.append(lognum+1)
            else:
                #print('con4')
                if num<revnorm:
                    num-=revnormm1
                    if lognum-1 in res:
                        return False 
                    res.append(lognum-1)                    
                elif num<revnormp1:
                    num-=revnorm
                    if lognum in res:
                        return False 
                    res.append(lognum)
                else:
                    num-=revnormp1
                    if lognum+1 in res:
                        return False 
                    res.append(lognum+1)
                       
            
def gift():
    for _ in range(t):
        n,k = list(map(int,input().split()))
        array=list(map(int,input().split()))
        gotarr=[]
        found=True
        for ele in array:
            logitnum=getit(ele,k)
            #print(ele,k,logitnum)
            if not found:
                break
            else:
                if ele:
                    if logitnum:
                        for nums in logitnum:
                            if nums not in gotarr:
                                gotarr.append(nums)
                            else:
                                found=False
                                break
                                
                    else:
                        found=False
        #print(gotarr)
        if found:
            yield 'YES'
        else:
            yield 'NO'


if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            
