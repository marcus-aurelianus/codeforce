def lis(arr): 
    n = len(arr) 
  
    # Declare the list (array) for LIS and initialize LIS 
    # values for all indexes 
    lis = [1]*n 
  
    # Compute optimized LIS values in bottom up manner 
    for i in range (1, n): 
        for j in range(0, i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
  
    # Initialize maximum to 0 to get the maximum of all 
    # LIS 
    maximum = 0
  
    # Pick maximum of all LIS values 
    for i in range(n): 
        maximum = max(maximum, lis[i]) 
  
    return maximum 
# end of lis function 
  
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__

def gift():
    for _ in range(t):
        n=int(input())
        array=list(map(int,input().split()))
        if n>=len(array):
            yield len(set(array))
                
        else:            
            yield lis(array*n)

if __name__ == '__main__':
    t= int(input())
    ans = gift()
    print(*ans,sep='\n')
