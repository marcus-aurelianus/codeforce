import time
import math
prime=[]
def rwh_primes2(n):
    # https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    if n==5:
        return [2,3,5]
    if n==3 or n==4:
        return [2,3]
    if n==2:
        return [2]
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n//3)
    sieve[0] = False
    for i in range(int(n**0.5)//3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)//3)      ::2*k]=[False]*((n//6-(k*k)//6-1)//k+1)
        sieve[(k*k+4*k-2*k*(i&1))//3::2*k]=[False]*((n//6-(k*k+4*k-2*k*(i&1))//6-1)//k+1)
    return [2,3] + [3*i+1|1 for i in range(1,n//3-correction) if sieve[i]]
def segmentedSieve(n):
    limit=int(math.floor(math.sqrt(n))+1)
    start = time.time()

    prime=rwh_primes2(limit)
    end = time.time()
    print(end-start)
    low = limit 
    high = limit * 2
    while low < n: 
        if high >= n: 
            high = n 
              
        # To mark primes in current range. A value in mark[i]  
        # will finally be False if 'i-low' is Not a prime,  
        # else True.  
        mark = [True for i in range(limit + 1)] 
          
        # Use the found primes by simpleSieve()  
        # to find primes in current range  
        for i in range(len(prime)): 
              
            # Find the minimum number in [low..high]  
            # that is a multiple of prime[i]  
            # (divisible by prime[i])  
            # For example, if low is 31 and prime[i] is 3,  
            # we start with 33.  
            loLim = int(math.floor(low / prime[i]) * 
                                         prime[i]) 
            if loLim < low: 
                loLim += prime[i] 
                  
            # Mark multiples of prime[i] in [low..high]:  
            # We are marking j - low for j, i.e. each number  
            # in range [low, high] is mapped to [0, high-low]  
            # so if range is [50, 100] marking 50 corresponds  
            # to marking 0, marking 51 corresponds to 1 and  
            # so on. In this way we need to allocate space  
            # only for range  
            for j in range(loLim, high, prime[i]): 
                mark[j - low] = False
                  
        # Numbers which are not marked as False are prime  

                  
        # Update low and high for next segment  
        low = low + limit 
        high = high + limit 
if __name__ == '__main__':
    start = time.time()
    segmentedSieve(1000000)
    end = time.time()
    print(end-start)
    start = time.time()
    print(rwh_primes2(1000000))
    end = time.time()
    print(end-start)
