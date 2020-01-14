lst=[2, 55, 56, 122, 213, 233, 3234, 4007]
lst.sort()
print(lst)
maxn=max(lst)
n=len(bin(maxn)[2:])
result= [0,float("inf")]
for ele in lst:
    auxi=n-len(bin(ele)[2:])
    print("0"*auxi+bin(ele)[2:],ele)
for i in range(maxn):
    temp=0
    for ele in lst:
        temp=max(temp,i^ele)
    if result[1]>temp:
        result=[i,min(result[1],temp)]
print("                ")
print(result)
print(bin(result[0])[2:])
print("                ")
for ele in lst:
    res=ele^result[0]
    auxi=n-len(bin(res)[2:])
    print("0"*auxi+bin(res)[2:],ele,res)
print("                ")       
print(bin(result[1])[2:])
