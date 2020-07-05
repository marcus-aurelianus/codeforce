# Python program to find 
# minimum sum of product  
# of two arrays with k 
# operations allowed on 
# first array. 
  
# Function to find the minimum product 
def minproduct(a,b,n,k): 
  
    diff = 0
    res = 0
    for i in range(n):  
  
        # Find product of current 
        # elements and update result. 
        pro = a[i] * b[i] 
        res = res + pro 
  
        # If both product and 
        # b[i] are negative, 
        # we must increase value 
        # of a[i] to minimize result. 
        if (pro < 0 and b[i] < 0): 
            temp = (a[i] + 2 * k) * b[i] 
  
        # If both product and 
        # a[i] are negative, 
        # we must decrease value 
        # of a[i] to minimize result. 
        elif (pro < 0 and a[i] < 0): 
            temp = (a[i] - 2 * k) * b[i] 
  
        # Similar to above two cases 
        # for positive product. 
        elif (pro > 0 and a[i] < 0): 
            temp = (a[i] + 2 * k) * b[i] 
        elif (pro > 0 and a[i] > 0): 
            temp = (a[i] - 2 * k) * b[i] 
  
        # Check if current difference 
        # becomes higher 
        # than the maximum difference so far. 
        d = abs(pro - temp) 
  
        if (d > diff): 
            diff = d        
    return res - diff 
  
# Driver function 
a = [ 4,4,4,4,4,4,2,2,2,2 ] 
b = [ 25,25,25,25,25,25,5,5,5,5,5 ] 
n = 10
k = 0
print(minproduct(a, b, n, k)) 
