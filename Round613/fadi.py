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
res=None

if n>30:
   some=12
else:
   some=2
if n==1:
   print("1 1")
else:
   for i in range(n//2-some,n):
       if res==None:
           if i==n:
               res=[1,n]
           else:

               for j in range(n//2-some+1,n):
                   if compute_lcm(fList[i],fList[j])==x:
                       res=[fList[i],fList[j]]
                       break
       else:
           if i<n:
               if fList[i]>=res[1]:
                   break
               else:
                   for j in range(n//2-some,n):
                       if compute_lcm(fList[i],fList[j])==x:
                           if max(fList[i],fList[j])<max(res):
                              res=[fList[i],fList[j]]
                           break

                  
               
       
   l, r = res
   print(str(l)+" "+str(r))

