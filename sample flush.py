import sys
 
n,k = map(int,input().split())
 
q = [i+1 for i in range(k+1)]
a = [None] * n
ind = 0
 
dic = {}
exist = []
 
for i in range(k+1):
 
    query = "?"
    for j in range(k+1):
        if i != j:
            query += " "
            query += str(q[j])
 
    print (query, flush = True)
 
    pos,num = map(int,input().split())
    if num not in exist:
        exist.append(num)
        dic[num] = 1
    else:
        dic[num] += 1
 
exist.sort()
print ("!" , dic[exist[-1]] , flush = True)
