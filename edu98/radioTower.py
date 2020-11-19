import math 
  
# Function to find modulo inverse of b. It returns  
# -1 when inverse doesn't  
# modInverse works for prime m 
def modInverse(b,m): 

    return pow(b, m - 2, m) 
  
  
# Function to compute a/b under modulo m  
def modDivide(a,b,m): 
    a = a % m 
    inv = modInverse(b,m) 
    return (inv*a) % m

n = int(input())

curr = 1
prev = 2
if n == 2 :
    fib = 1
elif n==3:
    fib = 2
else:
    for i in range(4,n+1):
        tem = curr
        curr = prev
        prev += tem
    fib = prev
if n==1:
    print(modDivide(1,2,998244353))
else:
    print(modDivide(fib,2**n,998244353))
