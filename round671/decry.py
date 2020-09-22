import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
from functools import reduce
from collections import defaultdict
import math
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
def gift():
    for _ in range(t):
        n = int(input())
        factList = list(factors(n))
        factList = sorted(factList)[1:]
        primeDic = defaultdict(lambda:[])

        primeLis = []
        for ele in factList:
            if isPrime(ele):
                primeDic[ele].append(ele)
                primeLis.append(ele)
            else:
                for key in primeDic:
                    if ele % key == 0:
                        primeDic[key].append(ele)
                        break
        m = len(primeLis)
        freeToGoLis = []
        freeToGo = defaultdict(lambda:[])
        for i in range(m):
            currPrime = primeLis[i]
            nextPrime = primeLis[(i+1)%m]
            if len(primeDic[currPrime])>2:
                counter = 0
                for ele in primeDic[currPrime]:
                    if ele%nextPrime!=0 and ele != currPrime or counter>=2:
                        freeToGo[ele] = currPrime
                    else:
                        counter += 1
            else:
                for ele in freeToGo:
                    if ele%currPrime==0 and ele%nextPrime==0:
                        where = freeToGo[ele]
                        del freeToGo[ele]
                        primeDic[where].remove(ele)
                        primeDic[currPrime].append(ele)
                        break
                        
        ans = []
        for ele in primeDic:
            ans.extend(primeDic[ele])
        res = 0
        leni = len(factList)
        for i in range(leni):
            currPrime = ans[i]
            nextPrime = ans[(i+1)%leni]
            if math.gcd(currPrime,nextPrime) == 1:
                res += 1
        
        yield " ".join([str(x) for x in ans])
        yield res
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
