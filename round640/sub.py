from collections import defaultdict 
  
# Function to find number of subarrays   
# with sum exactly equal to k.

def findSubarraySum(dila,arr, n):  
   
    # Dictionary to store number of subarrays  
    # starting from index zero having   
    # particular value of sum.  
    prevSum = defaultdict(lambda : 0) 
    
    res = 0 
    
    # Sum of elements so far.  
    currsum = 0 
    
    for i in range(0, n):   
    
        # Add current element to sum so far.  
        currsum += arr[i]  
    
        # If currsum is equal to desired sum,  
        # then a new subarray is found. So  
        # increase count of subarrays.
        biu=dila.get(currsum,False)
        if biu:
            res+=1
            dila[currsum]=False

        # currsum exceeds given sum by currsum  - sum. 
        # Find number of subarrays having   
        # this sum and exclude those subarrays  
        # from currsum by increasing count by   
        # same amount.  
        if (currsum - Sum) in prevSum: 
            res += prevSum[currsum - Sum]  
            
    
        # Add currsum value to count of   
        # different values of sum.  
        prevSum[currsum] += 1 
    print(prevSum)
    return res  
   
if __name__ == "__main__": 
  
    arr =  [3,1,4,1,5,9,2,6,5]
    dila={ i : True for i in arr }
    print(dila)
    n = len(arr)  
    print(findSubarraySum(dila,arr, n))  
      
# This code is contributed by Rituraj Jain 
