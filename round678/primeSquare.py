import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__
def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True
def gift():
    for _ in range(t):
        n = int(input())
        desireNum = 1
        for i in range(2,10):
            temDesire = (2**i)
            if is_prime((n-1)*temDesire+1):
                desireNum = temDesire
                break
        for i in range(n):
            yield " ".join(str(x) for x in [desireNum]*i+[1]+(n-i-1)*[desireNum])
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 1 2 2 2 2
