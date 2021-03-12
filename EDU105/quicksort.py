def partition(arr,low,high): 
    i = ( low-1 )          
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
  
 
# arr[] --> 
# low  --> 
# high  --> 
  
# 
def quickSort(arr,low,high): 
    if low < high: 
        index = partition(arr,low,high)
  
        quickSort(arr, low, index-1) 
        quickSort(arr, index+1, high) 
  
arr = [5454,2232,5523,2434,43,4343,2323,323,131535,545] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("after:") 
for i in range(n): 
    print ("%d" %arr[i]),
