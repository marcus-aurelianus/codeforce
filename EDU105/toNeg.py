def toNegativeBase(n, negBase): 
      
    # If n is zero then in any base it  
    # will be 0 only 
    if (n == 0): 
        return "0"
  
    converted = "01"
    while (n != 0): 
          
        # Get remainder by negative base,  
        # it can be negative also 
        remainder = n % (negBase) 
        n = int(n/negBase) 
  
        # if remainder is negative, add  
        # abs(base) to it and add 1 to n 
        if (remainder < 0): 
            remainder += ((-1) * negBase) 
            n += 1
  
        # convert remainder to string add 
        # into the result 
        converted = str(remainder) + converted 
          
    return converted 
  
# Driver Code 
if __name__ == '__main__': 
    n = -13
    negBase = -2
  
    print(toNegativeBase(n, negBase))
