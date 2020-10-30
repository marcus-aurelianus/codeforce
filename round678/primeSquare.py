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
        for i in range(n):
            posA = i
            posB = n-1-i
            if n%2==0 or (n%2 and abs(posA-posB)>2):
                thisRow = min(posA,posB)*[0]+[1]+(abs(posA-posB)-1)*[0]+[1]+(n-1-max(posA,posB))*[0]
            else:
                posMid = n//2
                thisRow = (posMid-1)*[0]+[1,1,1]+(n-1-posMid-1)*[0]
            yield " ".join(str(x) for x in thisRow)
if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
            


#"{} {} {}".format(maxele,minele,minele)
# 1 2 2 2 2
