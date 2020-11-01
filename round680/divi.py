import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
import math 

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
        for i in range(3,int(math.sqrt(n))+1,2):   
            if n % i== 0: 
                ans[i]+=1
                n = n // i
                break
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
                factors = primeFactors(xi)
                found = False
                while not found:
                    for ele in factors:
                        num, count = ele
                        if (xi//num)%pi:
                            yield xi//num
                            found = True
                            break
                    if found:
                        break
                    for i,ele in enumerate(factors):
                        num, count = ele
                        if count != 0:
                            xi = xi%num
                            factors[i]=(num,count-1)
        
                


        
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
