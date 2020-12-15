import math 
  
# Function to find modulo inverse of b. It returns  
# -1 when inverse doesn't  
# modInverse works for prime m 
def modInverse(b,m): 
    g = math.gcd(b, m)  
    if (g != 1): 
        # print("Inverse doesn't exist")  
        return -1
    else:  
        # If b and m are relatively prime,  
        # then modulo inverse is b^(m-2) mode m  
        return pow(b, m - 2, m) 
  
  
# Function to compute a/b under modulo m  
def modDivide(a,b,m): 
    a = a % m 
    inv = modInverse(b,m) 
    return (inv*a) % m

print(modDivide(1,32,998244353))
