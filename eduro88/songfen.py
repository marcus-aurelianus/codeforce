from sys import maxsize 
import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__ 
# Function to find the maximum contiguous subarray 
# and print its starting and end index

def maxSubArraySum(a,size): 
  
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    maxele=-float("inf")
    for i in range(0,size): 
        maxele=max(maxele,a[i])
        max_ending_here += a[i] 
        real_max=max_ending_here-maxele
        if max_so_far < real_max: 
            max_so_far = real_max
            #print(max_so_far)
            start = s 
            end = i 
  
        if max_ending_here < 0: 
            max_ending_here = 0
            s = i+1
            maxele=-float("inf")


    return max_so_far

def maxSubArraySum1(a,size): 
  
    max_so_far = -maxsize - 1
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    maxele=-float("inf")
    for i in range(0,size): 
        maxele=max(maxele,a[i])
        max_ending_here += a[i] 
        real_max=max_ending_here-maxele
        if max_so_far < real_max: 
            max_so_far = real_max
            #print(max_so_far)
            start = s 
            end = i 
  
        if real_max < 0: 
            max_ending_here = 0
            s = i+1
            maxele=-float("inf")

    if max_so_far==0:
        bibi=max(a)
        if bibi<0:
            return bibi
        else:
            return 0
    return max_so_far



n = int(input())
lst= list(map(int,input().split()))

print(max(maxSubArraySum(lst,n),maxSubArraySum1(lst,n)))
