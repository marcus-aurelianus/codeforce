import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

n=int(input())
lst = list(map(int,input().split()))

import bisect
def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return a[i]
    else:
        return None
def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect.bisect_right(a, x)
    if i != len(a):
        return a[i]
    else:
        return None
ina=[lst[0]]
dic={lst[0]:[0]}
for i in range(1,n):
    ele=lst[i]
    ina.append(ina[-1]+ele)

    pos=dic.get(ina[-1],[])
    pos.append(i)
    dic[ina[-1]]=pos

cum=0
res=0

#print(ina,dic)
for i in range(n):
    if lst[i]!=0:
        kap=dic.get(cum,None)
        kappa=dic.get(cum+lst[i],None)



        inamo=n
        bobo=n 
        print(kap,kappa,i)
        if kap:
            t1=find_ge(kap,i)
            if t1!=None:
                inamo=t1
        if kappa:
            t2=find_gt(kappa,i)
            if t2!=None:
                bobo=t2

        #print(i,inamo,bobo)         
        next0=min(inamo,bobo)
        
        res+=(next0-i)
        cum+=lst[i]
        print(i,next0,inamo,bobo,res)
    #print(i,res)
print(res)
    


            

