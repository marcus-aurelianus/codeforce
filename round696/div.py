import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    ans = []
    # Print all prime numbers 
    for p in range(2, n+1): 
        if prime[p]: 
            ans.append(p)
    return ans
primes = SieveOfEratosthenes(20011)
def gift():
    for _ in range(t):
        d = int(input())
        for ele in primes:
            if ele-1>=d:
                fPrime = ele
                break
        for ele in primes:
            if ele-fPrime>=d:
                sPrime = ele
                break
        yield fPrime*sPrime
            
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)

# yield " ".join([str(x) for x in ans])

