import math
from functools import reduce
x = int(input())
 
def compute_gcd(x, y):
   while(y):
       x, y = y, x % y
   return x
# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
 
res=None
fList=list(factors(x))
fList.sort()
n=len(fList)
#print(n//2)

#print(fList)
ans=[1,x]
s,e=n//2-1,n//2
Iter=True
while Iter:
    #print(s,e)
    if fList[s]==fList[e] or s==0 or e==n-1:
        Iter=False
        break
    else:
        for i in range(s,e):
            for j in range(i+1,e+1):
                #print(fList[i],fList[j])
                if compute_lcm(fList[i],fList[j])==x:
                    s,e=i,j
                    Iter=False
                    break
    if Iter:
        s-=1
        e+=1
print(fList[s],fList[e])
            
