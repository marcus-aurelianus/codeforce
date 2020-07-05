m=int(input())

num,mod=m//1000,m%1000

def doublefactorial(n): 
  
    if (n == 0 or n == 1): 
        return 1; 
    return n * doublefactorial(n - 2)%mod;
print(doublefactorial(num))

