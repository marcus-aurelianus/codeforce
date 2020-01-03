import sys
 
n,k = map(int,input().split())
 

 
dic = {}
exist = []
 
for i in range(k+1):
 
    query = "? "

    query += " ".join([str(ele+1) for ele in range(k+1) if ele!=i])
 
    print (query, flush = True)
 
    pos,num = map(int,input().split())
    if num not in exist:
        exist.append(num)
        dic[num] = 1
    else:
        dic[num] += 1
 
exist.sort()
print(dic,exist)
print ("!" , dic[exist[-1]] , flush = True)
