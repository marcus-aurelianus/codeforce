array=[1,3,3334,5454656,565]

n=len(array)
ans=0
for i in range(n):
    for j in range(i+1,n):
        ans^=(array[i]+array[j])
print(ans)
print(sum(array))

ina=len(bin(max(array))[2:])
lena=len(bin(ans)[2:])
print((ina-lena)*'0'+bin(ans)[2:])
for ele in array:
    lenb=len(bin(ele)[2:])
    print((ina-lenb)*'0'+bin(ele)[2:])


sum1 = 0
arr=array
for i in range(0, 32): 

    #  Count of zeros and ones 
    zc = 0
    oc = 0
       
    # Individual sum at each bit position 
    idsum = 0
    for j in range(0, n): 
        if (arr[j] % 2 == 0): 
            zc = zc + 1
              
        else: 
            oc = oc + 1
        arr[j] = int(arr[j] / 2) 
      
       
    # calculating individual bit sum  
    idsum = oc * zc * (1 << i) 

    # final sum     
    sum1 = sum1 + idsum;
print(sum1)
