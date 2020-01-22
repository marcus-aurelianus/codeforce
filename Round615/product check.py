import sys
from functools import reduce
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
def factors(n):    
    return list(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
res=[]
def product(n):
    for i in range (1,n):
        
        yn=factors(i)
        yn.sort()
        #print(yn)
        
        #if len(yn)>=7:
            #print ('YES')
            #print (str(yn[1])+' '+str(yn[2])+' '+str(int(n/yn[1]/yn[2])))
        if len(yn)>=3:
            #print ('NO')
            a,b=yn[1],yn[2]
            c=i//yn[1]//yn[2]
            d=i//yn[1]%yn[2]
            if c>1 and c!=a and c!=b and d==0:
                print (i,a,b,c)
                res.append(i)
product(1000)
print(len(res))
for ele in res:
    print(ele)

