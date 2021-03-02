def printNthElement(n) : 
      
    # create an array of size (n + 1) 
    arr =[0] * (n + 1); 
    arr[1] = 4
    arr[2] = 7
  
    for i in range(3, n + 1) : 
        # If i is odd 
        if (i % 2 != 0) : 
            arr[i] = arr[i // 2] * 10 + 4
        else : 
            arr[i] = arr[(i // 2) - 1] * 10 + 7
      
    return arr[n] 
      
# Driver code 
n = 6
print(printNthElement(n)) 

def printNthElement2(n) :
    ans = []
    while n>=1:
        if n&1:
            ans.append('4')
            n = (n-1)//2
        else:
            n = n//2-1
            ans.append('7')
    return int(''.join(ans))

print(printNthElement2(7))
