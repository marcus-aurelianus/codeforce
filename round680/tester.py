import math
from functools import reduce
from math import sqrt

from collections import defaultdict
# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 
    ans = defaultdict(lambda:0)
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        ans[2]+=1 
        n = n // 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used
    while n!=1:
        found=False
        for i in range(3,int(math.sqrt(n))+1,2):   
            if n % i== 0:
                found=True
                ans[i]+=1
                n = n // i
                break
        if not found:
            ans[n]+=1
            n = 1
    return list(ans.items())

print(primeFactors(270793475274034375//267605))
print(primeFactors(267605))
      
