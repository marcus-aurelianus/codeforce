import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math
from functools import reduce
from math import sqrt

def factors(n):
        step = 2 if n%2 else 1
        return set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

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


def gift():
    for _ in range(t):
        xi,pi = list(map(int,input().split()))


        if pi>xi:
            yield xi
        else:
            if xi%pi:
                yield xi
            else:
                #print(xi,pi)
                ans = 1

                pFactors = primeFactors(pi)
                #print(pFactors)
                for i in range(len(pFactors)):
                    counter=1
                    while True:
                        now = pFactors[i][0]**(counter)
                        if xi%(now)==0:
                            if (xi//now%pi):
                                ans = max(ans,xi//now)
                        else:
                            break
                        counter+=1
                        #print(i,counter)
                yield ans
                    


        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            

# 10000 100
# 100 100
# 2 2 5 5
# 2 2 5 5
#"{} {} {}".format(maxele,minele,minele)
