import math
print(math.log(42391158275216203514294433203,9))
def getit(num,base):
    res=[]
    while True:
        if num==0:
            return res
        else:
            lognum=int(math.log(num,base))
            revnorm=base**lognum
            revnormp1=base**(lognum+1)
            #print(res,lognum,revnorm,num)

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
                num-=revnorm
                if lognum in res:
                    return False 
                res.append(lognum)
print(getit(0,4)) 
